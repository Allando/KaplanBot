"""
This plugin will be the bot interrupting an ongoing conversation. 
"""

from disco.bot import Plugin
from time import sleep

class BudinPlugin(Plugin):
    @Plugin.listen('MessageCreate')
    def me_too_pls(self, event):
        if 'Overwatch' in event.message.content and '?' in event.message.content:
            sleep(5)
            event.reply("me 2, pls")

    @Plugin.listen('MessageCreate')
    def jeff(self, event):
        if "jeff" in event.message.content:
            event.reply("You, hailed?")
