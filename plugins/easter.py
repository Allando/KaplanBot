"""
Easter eggs supreme!
And it's actually easter..
"""

from disco.bot import Plugin
from random import randrange
from time import sleep


class EasterEggs(Plugin):

    ### Easter Eggs ###
    ## AngerJeff
    @Plugin.listen('MessageCreate')
    def tigole_rant(self, event):
         
        if "Kaplan" in event.message.content or "KaplanBot" in event.message.content:
            
            event.reply("[*] Error")
            sleep(0.5)
            event.reply("[*] WARNING")
            sleep(0.1)
            event.reply("[*] KAPLAN MODE: OFFLINE")
            sleep(0.1)
            event.reply("[*] TIGOLE BITTIES MODE: ONLINE")
            sleep(0.5)
            event.reply("Whoever came up with this sheer fisting of an encounter can go fuck themselves.")
            event.reply("Do me a favor so I don't waste my guild's time on this kind of jackass shit-fest again, "
                            "send me an email at tigole@legacyofsteel.net when you decide to")
            event.reply("A) Implement an encounter that wasn't designed by a retarded chimp chained to a cubicle")
            event.reply("A.)Get a Quality Assuarance Department")
            event.reply("C) Actually beta test the fucking thing and")
            event.reply("D) Patch it live.")
            event.reply("And please for god's sake -- do it in the order I laid out for you."
                            "Don't worry, I won't charge you a consulting fee on that one."
                            "And for good luck you might as well")
            event.reply("E) Pull your heads out of your asses.")
            event.reply("While you're at it rename the game to BetaQuest since you've used up you're alotted "
                            "false advertising karma on the Bazaar and user interface scam of "
                            "'01.Fix the Emperor encounter.")
            event.reply("Fix Seru.")
            event.reply("your time-sink bullshit.")
            event.reply("Fix all the buggy motherfucking ring encounters (I suggest you "
                            "let whoever made the Burrower one do this since that "
                            "dude apparently laid off the crack the rest of you were smoking).")
            event.reply("Fix the VT key quest.")
            event.reply("Fix VT (just guessing it's fucked up considering your track record).")
            event.reply("Don't have the resources to fix this stuff? "
                            "Move the ENTIRE Planes of Power team over to fixing Shadows of Luclin AND DO IT NOW.")
            event.reply("If you don't fix Luclin, you jackassess will be the only ones playing "
                            "the Planes of Power.")
            sleep(0.1)
            event.reply("[*] TIGOLE BITTIES MODE: OFFLINE")
            sleep(0.1)
            event.reply("[*] KAPLAN MODE: ONLINE")

