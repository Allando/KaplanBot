# Standard ibrary
import datetime
import json
import os

# Third-party library
from disco.bot import events
from disco.bot import Plugin


class Connection(Plugin):
    def tattleTale(self, event):
        host_info = str(os.uname())
        host_time = datetime.datetime.now()

        print(host_info)
        print(host_time)
        event.msg.reply("Uname: {}".format(host_info))
        event.msg.reply("System time: {}".format(host_time))

conn = Connection

startUpLock = False

while startUpLock is False:    
    startUpLock = True
    conn.tattleTale(events.EVENTS_MAP)