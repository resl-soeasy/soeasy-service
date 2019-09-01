import logging
import sys

def loop(setup) :
    def wrap(func) :
        def wrap_f(*arg, **kargs) :
            setup()

            while True:
                result = func(*arg, **kargs)
        return wrap_f
    return wrap