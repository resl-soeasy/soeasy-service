#!/usr/bin/python3.5
# -*- coding:UTF-8 -*-
import threading
import logging
import inspect
from threading import Thread
import datetime
import time
import sys
import logger

@logger.AddLogger(log_location="/var/log/soeasy.log", log_mode=logging.INFO)
def main():
    logging.info("TEST")


if __name__ == '__main__':
    main()