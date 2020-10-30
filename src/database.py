import sqlite3
from os import path
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Database:
	def __init__(self):
		
		self.path = "./data.db"
		self.conn = None
		self.reset = False
		if not path.exists(self.path):
			self.reset = True
			logger.info("no database detected")

		try:
			self.conn = sqlite3.connect(self.path)
			if self.reset:
				self.create_new_db()
				self.reset = False
		except Exception as e:
			logging.ERROR(e)
		
	def create_new_db(self):
		logger.info("creating database...")
		create_event_table = """ CREATE TABLE event (
			id integer PRIMARY KEY,
			name title NOT NULL,
			begin_date text,
			end_date text
			); """
		create_task_table = """ CREATE TABLE task (
			id integer PRIMARY KEY,
			name title NOT NULL,
			begin_date text,
			end_date text
			); """
		try:
			c = self.conn.cursor()
			c.execute(create_event_table)
			c.execute(create_task_table)
		except Exception as e:
			logging.ERROR(e)


	def close(self):
		if self.conn:
			self.conn.close()
