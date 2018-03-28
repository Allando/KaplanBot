"""
This is the awesome KaplanBot.
It's purpose is to bring do something cool
"""

from disco.bot import Plugin
from time import sleep


class BasicPlugin(Plugin):
    ### Console ###
    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('Pong!')

    @Plugin.command('Help')
    def command_help(self, event):
        event.msg.reply("CONSOLE\n"
                        "Help : Displays this message\n"
                        "Ping : Send a ping request to KaplanBot")
        event.msg.reply("BASIC COMMANDS\n"
                        "Hello : Don't be a dick... Say Hello once a while.\n"
                        "Tell a joke : Displays a joke\n"
                        "Rant : ERROR: UNKNOWN FEATURE")

    ### Basic commands ###
    @Plugin.command('Hello')
    def command_hello(self, event):
        event.msg.reply('Hi, this is Jeff from the overwatch team')

    # Jokes
    @Plugin.command('Tell a joke')
    def command_random_joke(self, event):
        event.msg.reply('There are no good Hanzo jokes...')
        sleep(1)
        event.msg.reply('... Just like there are no good Hanzomains')


