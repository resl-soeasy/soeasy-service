import logging
from soeasy import dbhandler, command, helper
from abc import *

GPIO_SYSFS = "/sys/class/gpio/gpio"

class GpioDigitalCommand(command.Command):
    def __init__(self):
        logging.info("GPIO Command Start")

    def set_value(self, value):
        logging.info("Set Value (Index : {}, Value {}".format(self.index, value))
        helper.ShellCommand(command="echo '{}' > {}{}/value".format(value, GPIO_SYSFS, self.index), exit=False)

    def get_value(self):
        result = helper.ShellCommand(command="cat {}{}/value".format(GPIO_SYSFS, self.index), exit=False)
        return result