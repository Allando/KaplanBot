#!/bin/python

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

    ### Insults ###
    @Plugin.command('Rant')
    def command_insult(self, event):
        event.msg.reply("[*] Error")
        sleep(0.5)
        event.msg.reply("[*] WARNING")
        sleep(0.25)
        event.msg.reply("[*] KAPLAN MODE: OFFLINE")
        sleep(0.25)
        event.msg.reply("[*] TIGOLE MODE: ONLINE")
        sleep(0.5)
        event.msg.reply("Whoever came up with this sheer fisting of an encounter can go fuck themselves.")
        event.msg.reply("Do me a favor so I don't waste my guild's time on this kind of jackass shit-fest again, "
                        "send me an email at tigole@legacyofsteel.net when you decide to")
        event.msg.reply("A) Implement an encounter that wasn't designed by a retarded chimp chained to a cubicle")
        event.msg.reply("A.)Get a Quality Assuarance Department")
        event.msg.reply("C) Actually beta test the fucking thing and")
        event.msg.reply("D) Patch it live.")
        event.msg.reply("And please for god's sake -- do it in the order I laid out for you."
                        "Don't worry, I won't charge you a consulting fee on that one."
                        "And for good luck you might as well")
        event.msg.reply("E) Pull your heads out of your asses.")
        sleep(0.5)
        event.msg.reply("While you're at it rename the game to BetaQuest since you've used up you're alotted "
                        "false advertising karma on the Bazaar and user interface scam of "
                        "'01.Fix the Emperor encounter.")
        event.msg.reply("Fix Seru.")
        event.msg.reply("your time-sink bullshit.")
        event.msg.reply("Fix all the buggy motherfucking ring encounters (I suggest you "
                        "let whoever made the Burrower one do this since that "
                        "dude apparently laid off the crack the rest of you were smoking).")
        event.msg.reply("Fix the VT key quest.")
        event.msg.reply("Fix VT (just guessing it's fucked up considering your track record).")
        event.msg.reply("Don't have the resources to fix this stuff? "
                        "Move the ENTIRE Planes of Power team over to fixing Shadows of Luclin AND DO IT NOW.")
        event.msg.reply("If you don't fix Luclin, you jackassess will be the only ones playing "
                        "the Planes of Power.")
        sleep(0.5)
        event.msg.reply("[*] TIGOLE MODE: OFFLINE")
        sleep(0.25)
        event.msg.reply("[*] KAPLAN MODE: ONLINE")
