# -*- coding:utf-8 -*-
import logging
import logging.config

class Logger:
	def __init__(self, log_location, log_mode=logging.INFO):
		logging.basicConfig(format="[%(asctime)s] [%(process)s] [%(filename)-20.20s:%(lineno)-7.7s] %(levelname)7.7s - %(message)s", level=log_mode, handlers=[
			logging.FileHandler(log_location),
			logging.StreamHandler()
		])


def AddLogger(log_location, log_mode) :
    def wrap(func) :
        def wrap_f(*arg, **kargs) :
            Logger(log_location=log_location, log_mode=log_mode)
            result = func(*arg, **kargs)

            return result
        return wrap_f
    return wrap