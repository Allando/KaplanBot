#!/bin/python

"""
This is the awesome KaplanBot.
It's purpose is to bring do something cool
"""

from disco.bot import Plugin


class TutorialPlugin(Plugin):
    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('Pong!')
