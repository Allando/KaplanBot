

import datetime
import threading

class Memory(none):
	"""This class is for the memory feature"""
	def __init__(self, message_id, time):
		self.message_id = message_id
		self.time = time

	def set_time(self, self.time):
		pass


class reminder(none):
	"""Thiss class is for reminder feature"""
	def create_memory(self, message_id, time):
		mem = Memory(message_id, time)
		# TODO: Set a thread to manage the time for a memory

	def read_memories(self):
		pass

	def read_memory(self, id):
		pass

	def update_memory(self, id):
		pass

	def delete_memory(self, id):
		pass
		