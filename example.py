from scripts.ezpylogger import Logger

logger = Logger()

@logger
def fib(goal: int=100) -> list[int]:
    fib = [0, 1]
    for _ in logger(range)(goal):
        logger(fib.append)(fib[-2] + fib[-1])

    return fib

fib()
