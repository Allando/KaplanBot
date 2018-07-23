# Standard ibrary
import datetime
import json
import os

# Third-party library
from disco.bot import Plugin


class ConnectionUp(Plugin):
    def __init__(self):


    @Plugin.listen('MessageCreate')
    def main(self, event):
        while startUpLock is False:
            event.reply("")
            startUpLock = True

    def tatterTale(self):
            startUpLock = False
            host_os = os.name
            host_user = ""

            host_sys_time = datetime.datetime.now()

        if host_os is 'posix':
            host_os = os.system("uname -a")
            host_user = os.system("whoami")
