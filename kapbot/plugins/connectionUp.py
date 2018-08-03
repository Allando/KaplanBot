# Standard ibrary
import datetime
import json
import os

# Third-party library
from disco.bot import Plugin
from disco.gateway import GatewayClient

class Connection(Plugin):
    def listenForConnection(self, event):
        startUpLock = False

        while startUpLock is False:
            if GatewayClient.handle_hello():
                startUpLock = True
                tatterTale()

    def tatterTale(self):
        host_os = os.name
        host_user = ""

        host_sys_time = datetime.datetime.now()

        if host_os is 'posix':
            host_os = os.system("uname -a")
            host_user = os.system("whoami")

    

        