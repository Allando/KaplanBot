# Standard ibrar
import asyncio
import datetime
import json
import os

# Third-party library
import disco

class TattleTale:
		
async def on_startup():
	host_info = str(os.uname())
	host_time = datetime.datetime.now()

	event = """Uname: {}
	System time: {}
	--------------------""".format(host_info, host_time)

	await with open("logger.txt", "a") as fp:
		fp.writelines(event)

	await client.send_message(event)


async def message_log(chan=None, duration=None):
	pass
