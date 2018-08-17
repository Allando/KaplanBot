"""
Info:
	Author: Allando
	Github: https://github.com/Allando/KaplanBot

Description:

"""

# Standard library
import asyncio
from random import randrange
from time import sleep

# KaplanBot modules
from TattleTale import *
from Jokes import *

# Third-party library
import discord

class KaplanBot(discord.Client):
	"""docstring for KaplanBot"""
	def __init__(self, arg):
		super(KaplanBot, self).__init__()
		self.arg = arg
	
	tattleTale = TattleTale
	jokes = Jokes

	@client.event
	async def on_ready(self):
		tattleTale()


	@client.event
	async def on_message(self, message):
		if message.content.startswith('!test'):
			counter = 0
			tmp = await client.send_message(message.channel, 'Calculating messages...')
			async for log in client.logs_from(message.channel, limit=100):
				if log.author == message.author:
					counter += 1
					await client.edit_message(tmp, 'You have {} messages.'.format(counter))
				elif message.content.startswith('!sleep'):
					await asyncio.sleep(5)
					await client.send_message(message.channel, 'Done sleeping')
		elif message.content.startswith('!hello'):
			client.send_message(message.channel,"Hi, this is Jeff from the Overwatch team")
		elif message.content.startswith('!joke'):
			jokes.tell_joke()
		elif message.content.startswith('KaplanBot') or message.content.startswith('Kaplan'):
			self.tigole()
		elif message.content.startswith('Hacker') or message.content.startswith('hacking'):
			client.send_message(message.channel,"@everyone\nUh oh, looks like KaplanBot got compromised!\nOh TheIppo1000, you dummy, putting servers at risk and everything, classic!\nLooks like our buddy here will have to shoot itself in the face.\nOh well, everyone wave KaplanBot a goodbye, you will be missed! (most likely not)")
		elif message.content.startswith('Overwatch'):
			client.send_message(messages.channel, "You, hailed?")


	def tigole(self):
		if 5 is randrange(5000);
			client.send_message(message.channel,"[*] Error")
	        sleep(0.5)
	        client.send_message(message.channel,"[*] WARNING")
	        sleep(0.1)
	        client.send_message(message.channel,"[*] KAPLAN MODE: OFFLINE")
	        sleep(0.1)
	        client.send_message(message.channel,"[*] TIGOLE BITTIES MODE: ONLINE")
	        sleep(0.5)
	        client.send_message(message.channel,"Whoever came up with this sheer fisting of an encounter can go fuck themselves.")
	        client.send_message(message.channel,"Do me a favor so I don't waste my guild's time on this kind of jackass shit-fest again, "
	                        "send me an email at tigole@legacyofsteel.net when you decide to")
	        client.send_message(message.channel,"A) Implement an encounter that wasn't designed by a retarded chimp chained to a cubicle")
	        client.send_message(message.channel,"A.)Get a Quality Assuarance Department")
	        client.send_message(message.channel,"C) Actually beta test the fucking thing and")
	        client.send_message(message.channel,"D) Patch it live.")
	        client.send_message(message.channel,"And please for god's sake -- do it in the order I laid out for you."
	                        "Don't worry, I won't charge you a consulting fee on that one."
	                        "And for good luck you might as well")
	        client.send_message(message.channel,"E) Pull your heads out of your asses.")
	        client.send_message(message.channel,"While you're at it rename the game to BetaQuest since you've used up you're alotted "
	                        "false advertising karma on the Bazaar and user interface scam of "
	                        "'01.Fix the Emperor encounter.")
	        client.send_message(message.channel,"Fix Seru.")
	        client.send_message(message.channel,"your time-sink bullshit.")
	        client.send_message(message.channel,"Fix all the buggy motherfucking ring encounters (I suggest you "
	                        "let whoever made the Burrower one do this since that "
	                        "dude apparently laid off the crack the rest of you were smoking).")
	        client.send_message(message.channel,"Fix the VT key quest.")
	        client.send_message(message.channel,"Fix VT (just guessing it's fucked up considering your track record).")
	        client.send_message(message.channel,"Don't have the resources to fix this stuff? "
	                    "Move the ENTIRE Planes of Power team over to fixing Shadows of Luclin AND DO IT NOW.")
	        client.send_message(message.channel,"If you don't fix Luclin, you jackassess will be the only ones playing "
	                        "the Planes of Power.")
	        sleep(0.1)
	        client.send_message(message.channel,"[*] TIGOLE BITTIES MODE: OFFLINE")
	        sleep(0.1)
	        client.send_message(message.channel,"[*] KAPLAN MODE: ONLINE")




