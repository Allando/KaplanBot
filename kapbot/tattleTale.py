# Standard ibrar
import asyncio
import datetime
import json
import os

class TattleTale:
	def __init__(self):
		self.logPath = "libs/accessLog.txt"
		
	def on_startup(self):
		host_info = str(os.uname())
		host_time = datetime.datetime.now()

		event = """Uname: {}
		System time: {}
		--------------------""".format(host_info, host_time)

		with open(self.logPath, "a") as fp:
			fp.writeline(event)

		print(event)


	async def message_log(self, chan=None, duration=None):
		pass
