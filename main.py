#!/usr/bin/python3.5
# -*- coding:UTF-8 -*-
import threading
import logging
import inspect
from threading import Thread
import datetime
import time
import sys
from soeasy import configure, logger

class Init:
    def configure(self):
        self.configure = configure.Configure()
        self.configure.get_gpio_list()

@logger.AddLogger(log_location="/var/log/soeasy.log", log_mode=logging.INFO)
def main():
    Init().configure()

if __name__ == '__main__':
    main()