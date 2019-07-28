import logging
from soeasy import dbhandler, command, helper
from abc import *

GPIO_SYSFS = "/sys/class/gpio/gpio"

class GpioDigitalCommand(command.Command, dbhandler.DBHandler):
    def __init__(self):
        dbhandler.DBHandler.__init__(self)
        logging.info("GPIO Command Start")

    def set_value(self, value):
        logging.info("Set Value (Index : {}, Value {}".format(self.index, value))
        logging.info("echo '{}' > {}{}/value".format(value, GPIO_SYSFS, self.index))
        helper.ShellCommand(command="echo '{}' > {}{}/value".format(value, GPIO_SYSFS, self.index), exit=True)

        result =self.cursor.execute("UPDATE pinmap SET V={} WHERE phy={}".format(value, self.index), "")
        self.mydb.commit()

    def get_value(self):
        result = helper.ShellCommand(command="cat {}{}/value".format(GPIO_SYSFS, self.index), exit=True)
        logging.info("cat {}{}/value".format(GPIO_SYSFS, self.index))
        return result