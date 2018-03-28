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


    @Plugin.command('')
    def command_empty(self, event):
        event.msg.reply('You know; you must write a command') 

    #TODO: Integrate neural network
    """
    command_goodbot and command_badbot will have purpose with a future neural network integration.
    
    Commands are for rating a KaplanBot's previous action.
    Where giving a bad rating will result in it is less likely for the bot to perform the same action again.
    """
    @Plugin.command('Good bot')
    def command_goodbot(self, event):
        event.msg.reply('Thank you very much')

    @Plugin.command('Bad bot')
    def command_badbot(self, event):
        event.msg.reply('Well, fuck you too', event.user.mention())

    # Jokes
    @Plugin.command('Tell a joke')
    def command_random_joke(self, event):
        event.msg.reply('There are no good Hanzo jokes...')
        sleep(1)
        event.msg.reply('... Just like there are no good Hanzomains')


