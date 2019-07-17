import subprocess
import time
import logging
import sys

def ShellCommand(command, exit):
    package_subprocess = subprocess.Popen(command, shell=True, close_fds=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    package_subprocess.wait()
    out, err = package_subprocess.communicate()

    if exit == True:
        if package_subprocess.returncode == 0:
            logging.info("Command [{}] Success".format(command))
        else:
            logging.error("Command [{}] Failed (message(out): {}, message(err): {})".format(command, out, err))
            sys.exit(1)

    else:
        return {"return_code":package_subprocess.returncode, "out":out, "err":err}