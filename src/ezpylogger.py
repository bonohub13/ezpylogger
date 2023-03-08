from sys import argv
from datetime import datetime
from pathlib import Path


class Logger:
    '''
    Creates an instance of a logger that logs function calls, arguments
    and keywords passed to the function.
    Logs the function in the format below by default.
    > [YYYY-mm-dd HH:MM:SS.microseconds] function(a, b, c=d, e=f)
    - - -
    Arguments | keywords:
        logs_dir:   Absolute path to output logs
        >           (default: current working directory)
        src_filename: Name of python script running
        >           (default: value of sys.argv[0][:-3])
        runtime_fmt: Format string for the runtime of function to log
        >           (default: "%Y-%m-%d %H:%M:%S")
        filename_fmt: Format string for the runtime of script
        >           (default: "%Y%m%d_%H%M%S")
    Return:
        None
    ```
    '''

    filename = ""
    runtime_fmt = ""
    logger_invoked = False

    now = datetime.now

    def __init__(self,
                 logs_dir: str="",
                 src_filename: str=argv[0][:-3],
                 runtime_fmt: str="%Y-%m-%d %H:%M:%S.%f",
                 filename_fmt: str="%Y%m%d_%H%M%S",
                 print_func=print) -> None:
        # If logs_dir is default create logs directory on the
        # current working directory
        if logs_dir == "":
            Path.mkdir(Path.cwd() / 'logs', parents=True, exist_ok=True)
        else:
            Path.mkdir(Path(f'{logs_dir}/logs'))

        # If Logger is initialized or called the first time,
        # initialize the value
        if not Logger.logger_invoked and \
                Logger.filename == "" and \
                Logger.runtime_fmt == "":
            Logger.filename = "{}/logs/{}-{}.log".format(
                    "." if logs_dir == "" else logs_dir,
                    src_filename,
                    self.now().strftime(filename_fmt))
            Logger.runtime_fmt = runtime_fmt
            Logger.print = print_func
            Logger.logger_invoked = True

    def __call__(self, func):
        def dec(*args, **kwargs):
            # Time of function call
            # Created before function because the function may be doing some
            # heavy computational work.
            runtime = self.now().strftime(Logger.runtime_fmt)
            rv = func(*args, **kwargs)
            self.__log(func, runtime, *args, **kwargs)

            return rv
        return dec

    def __log(self, func, runtime: str, *args, **kwargs):
        log_msg = "[{}] {}({})".format(
                runtime,
                self.__f_name(func),
                self.__parse_args(*args, **kwargs))
        with open(Logger.filename, 'a') as f:
            f.writelines(f"{log_msg}\n")
        Logger.print(log_msg)

    def __f_name(self, func) -> str:
        # Returns the class name of the method by default
        # If the function is not a method of an object, it returns the
        # name of the function
        try:
            return func.__qualname__
        except AttributeError:
            return func.__class__.__name__

    def __parse_args(self, *args, **kwargs) -> str:
        args_str = ", ".join([str(arg) for arg in args])
        kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs])

        if args_str == kwargs_str:
            return ""
        elif args == "":
            return kwargs_str
        elif kwargs_str == "":
            return args_str
        else:
            return f"{args_str}, {kwargs_str}"
