# Standard ibrary
import datetime
import json
import os

# Third-party library
from disco.bot import Plugin
from disco.gateway import GatewayClient
from disco.util.logging import LoggingClass 

class ConnectionUp(Plugin):
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

    def listenForConnection(self):
        pass