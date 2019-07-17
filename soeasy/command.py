import logging
from soeasy import dbhandler, helper
from abc import *

GPIO_SYSFS = "/sys/class/gpio"

class Command(dbhandler.DBHandler):

    def __init__(self):
        self.index      = 0
        self.direction  = "in"
        self.value      = 0

    def set_configure(self, index=0, direction="out", drive="strong"):
        ## Direction
        self.index = index
        helper.ShellCommand("echo '{}' > {}/export".format(self.index, GPIO_SYSFS), exit=False)
        helper.ShellCommand(command="echo '{}' > {}/gpio{}/direction".format(direction, GPIO_SYSFS, index), exit=False)

    @abstractmethod
    def set_value(self, value=0):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def value(self):
        pass