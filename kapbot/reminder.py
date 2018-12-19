

import datetime
import json
import threading

class Memory(none):
	"""This class is for the memory feature"""
	def __init__(self, message_id, time):
		self.message_id = message_id
		self.time = time

	def set_time(self, self.time):
		pass


class reminder(none):
	index = 0
	"""Thiss class is for reminder feature"""
	def create_memory(self, message_id, time):
		mem = Memory(message_id, time)

		mem = json.dumps({'message_id': mem.message_id, 'reminder_time': mem.time})

		with open(pathToFile, "a") as fs:
			fs.write(mem)

		# TODO: Set a thread to manage the time for a memory

	def read_memories(self):
		with open(pathToFile, "r") as fs:
			memoriesObjList = fs.read()
			memoriesList = []
			for memory in memoriesObjList:
				mem = Memory(memory['message_id'], memory['reminder_time'])
				memoriesList.append(mem)
			return memoriesList

	def read_memory(self, _id):
		with open(pathToFile, "r") as fs:
			memoriesObjList = fs.read()
			for memory in memoriesObjList:
				if memory['message_id'] is _id:
					mem = Memory(memory['message_id'], memory['reminder_time'])
					return mem

	def update_memory(self, message_id, time):
		mem = Memory(message_id, time)
		mem = json.dumps

		with open(pathToFile, "r") as fr:
			memoriesObjList = fs.read()
			for memory in memoriesObjList:
				if memory['message_id'] is _id:



	def delete_memory(self, id):
		pass
	