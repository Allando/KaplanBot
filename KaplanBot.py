#!/bin/python

"""
This is the awesome KaplanBot.
It's purpose is to bring do something cool
"""

# Standard library
import asyncio

# Third party library
import discord


client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as\nUsername {}\nUserid {}")
    print("-" * 50)


@client.event
async def on_message(message):
    if message.centent.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

TOKEN = ""

client.run(TOKEN)

