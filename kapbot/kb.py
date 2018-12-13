#!/bin/python

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
from tattleTale import *
from jokes import *

# Third-party library
import discord


client = discord.Client()
	
tattleTale = TattleTale
jokes = Jokes


@client.event
async def on_ready():
		host_info = str(os.uname())
		host_time = datetime.datetime.now()

		event = "System time: {}\nUname: {}\n{}".format(host_time, host_info, '-' * 50)

		with open("libs/accessLog.txt", "a") as fp:
			fp.write(event + '\n')

		print(client.user.name)
		print(client.user.id)

		print(event)


@client.event
async def on_message(message):
	if message.content.startswith('!hello'):
		await client.send_message(message.channel,"Hi, this is Jeff from the Overwatch team")

	elif message.content.startswith('!joke'):
		jokes.tell_joke()

	elif message.content.startswith('KaplanBot') or message.content.startswith('Kaplan'):
		# It would be cool to have this seperated somewhere else yea..
		
		luckyNumber = 5
		numberRange = 5

		if luckyNumber is randrange(numberRange):
			print("Kaplan lottery: WINNING!!")
			await client.send_message(message.channel,"[*] Error")
			sleep(0.5)
			await client.send_message(message.channel,"[*] WARNING")
			sleep(0.1)
			await client.send_message(message.channel,"[*] KAPLAN MODE: OFFLINE")
			sleep(0.1)
			await client.send_message(message.channel,"[*] TIGOLE BITTIES MODE: ONLINE")
			sleep(0.5)
			await client.send_message(message.channel,"Whoever came up with this sheer fisting of an encounter can go fuck themselves.")
			await client.send_message(message.channel,"Do me a favor so I don't waste my guild's time on this kind of jackass shit-fest again, "
				"send me an email at tigole@legacyofsteel.net when you decide to")
			await client.send_message(message.channel,"A) Implement an encounter that wasn't designed by a retarded chimp chained to a cubicle")
			await client.send_message(message.channel,"A.)Get a Quality Assuarance Department")
			await client.send_message(message.channel,"C) Actually beta test the fucking thing and")
			await client.send_message(message.channel,"D) Patch it live.")
			await client.send_message(message.channel,"And please for god's sake -- do it in the order I laid out for you."
				"Don't worry, I won't charge you a consulting fee on that one."
				"And for good luck you might as well")
			await client.send_message(message.channel,"E) Pull your heads out of your asses.")
			await client.send_message(message.channel,"While you're at it rename the game to BetaQuest since you've used up you're alotted "
				"false advertising karma on the Bazaar and user interface scam of "
				"'01.Fix the Emperor encounter.")
			await client.send_message(message.channel,"Fix Seru.")
			await client.send_message(message.channel,"your time-sink bullshit.")
			await client.send_message(message.channel,"Fix all the buggy motherfucking ring encounters (I suggest you "
				"let whoever made the Burrower one do this since that "
				"dude apparently laid off the crack the rest of you were smoking).")
			await client.send_message(message.channel,"Fix the VT key quest.")
			await client.send_message(message.channel,"Fix VT (just guessing it's fucked up considering your track record).")
			await client.send_message(message.channel,"Don't have the resources to fix this stuff? "
				"Move the ENTIRE Planes of Power team over to fixing Shadows of Luclin AND DO IT NOW.")
			await client.send_message(message.channel,"If you don't fix Luclin, you jackassess will be the only ones playing "
				"the Planes of Power.")
			sleep(0.1)
			await client.send_message(message.channel,"[*] TIGOLE BITTIES MODE: OFFLINE")
			sleep(0.1)
			await client.send_message(message.channel,"[*] KAPLAN MODE: ONLINE")
		else:
			print("Kaplan lottery: FAILED!")

	elif message.content.startswith('Hacker') or message.content.startswith('hacking'):
		await client.send_message(message.channel,"@everyone\nUh oh, looks like KaplanBot got compromised!\nOh TheIppo1000, you dummy, putting servers at risk and everything, classic!\nLooks like our buddy here will have to shoot itself in the face.\nOh well, everyone wave KaplanBot a goodbye, you will be missed! (most likely not)")

	elif message.content.startswith('Overwatch?') or message.content.startswith('OW?'):
		await client.send_message(message.channel,"Me too pls")

	elif message.content.startswith('!remindme') or message.content.startswith('!rme'):
		pass
		# Remind me

	elif message.content.startswith('!help') or message.content.startswith('!h'):
		help_msg = ""
		help_msg = help_msg(message)
		await client.send_message(message.channel, help_msg)

@client.event
async def create_stream_player():
	print("value")

def help_msg(message):
	msg = "KaplanBot HELP"
	print(msg)
	return msg


with open("token.txt", "r") as f:
	client.run(f.read())
