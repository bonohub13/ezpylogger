# ezpylogger: Logging made simpler
- - -
## What is this?
This is an easy to use, logging library that can log function calls of ANY functions! \
This includes functions that you've made, functions that have been predefined. (Like any functions/methods that are included in other libraries)

## How do you use this?
Simple, just import the ezpylogger module and use the Logger to log function calls. \
Example:
``` python
from ezpylogger import Logger
from time import sleep

@Logger()
def add(a, b):
    return a + b

class Mul:
    logger = Logger()

    def __init__(self):
        pass

    @logger
    def __call__(self, *args, **kwargs):
        numbers = [ arg if arg.__class__.__name__ == 'int' or arg.__class__.__name__ == 'float' else 1 for arg in args ]
        rv = [1]
        for number in numbers:
            rv[0] *= number

        # Some very heavy computational task
        self.logger(sleep)(30)

        return rv + numbers

seven = add(3, 4)
prod = Mul()(1, 2, 3, 4, 5, 6, 7, 0.08, 0.69, 4.20)
```
