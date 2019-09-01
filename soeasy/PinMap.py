import logging
from soeasy import dbhandler, command, helper
from abc import *

GPIO_SYSFS = "/sys/class/gpio/"

def setDigitalMap(index=0, direction="out"):
    helper.ShellCommand("echo '{}' > {}/unexport".format(index, GPIO_SYSFS), exit=False)
    helper.ShellCommand("echo '{}' > {}/export".format(index, GPIO_SYSFS), exit=False)
    helper.ShellCommand(command="echo '{}' > {}/gpio{}/direction".format(direction, GPIO_SYSFS, index), exit=False)

def write(index=0, value=True):
    logging.info("Set Value (Index : {}, Value {}".format(index, value))
    logging.info("echo '{}' > {}gpio{}/value".format(value, GPIO_SYSFS, index))
    helper.ShellCommand(command="echo '{}' > {}gpio{}/value".format(value, GPIO_SYSFS, index), exit=True)

def read(index=0):
    result = helper.ShellCommand(command="cat {}gpio{}/value".format(GPIO_SYSFS, index), exit=True)
    return result["out"].decode("utf-8")