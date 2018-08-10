# Standard ibrary
import datetime
import json
import os

# Third-party library
from disco.bot import Plugin
from disco.util.logging import LoggingClass

class Connection(Plugin):
    @Plugin.command("j")
    def listenForConnection(self, event):
        startUpLock = False

        while startUpLock is False:
            if LoggingClass.log() is 'Received HELLO, starting heartbeater...':
                startUpLock = True
                tattleTale()

    @Plugin.command("h")
    def tattleTale(self, event):
        host_os = os.name()
        host_user = ""

        host_sys_time = datetime.datetime.now()

        if host_os is 'posix':
            host_os = os.system("uname -a")
            host_user = os.system("whoami")


            event.msg.reply(host_os)
            event.msg.reply(host_user)
            event.msg.reply(host_sys_time)

    

        