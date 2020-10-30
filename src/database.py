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
		create_event_table = """ CREATE TABLE events (
			id integer PRIMARY KEY autoincrement,
			title text NOT NULL,
			day integer NOT NULL,
			start_hour integer NOT NULL,
			start_minute integer NOT NULL,
			end_hour integer NOT NULL,
			end_minute integer NOT NULL,
			freq text NOT NULL,
			date text
			); """
		create_task_table = """ CREATE TABLE tasks (
			id integer PRIMARY KEY autoincrement,
			title text NOT NULL,
			day integer NOT NULL,
			hour integer NOT NULL,
			minute integer NOT NULL,
			freq text NOT NULL,
			date text,
			done integer
			); """
		try:
			c = self.conn.cursor()
			c.execute(create_event_table)
			c.execute(create_task_table)
		except Exception as e:
			logging.ERROR(e)

	def new_event(self, title, day, s_h, s_m, e_h, e_m, freq, date=None):
		sql = ''' INSERT INTO events 
		(title,day,start_hour,start_minute,end_hour,end_minute,freq,date)
        VALUES(?,?,?,?,?,?,?,?) '''
		cur = self.conn.cursor()
		cur.execute(sql, (title, day, s_h, s_m, e_h, e_m, freq, date))
		self.conn.commit()
		return cur.lastrowid

	def new_task(self, title, day, hour, minute, freq, date=None, done=0):
		sql = ''' INSERT INTO tasks (title,day,hour,minute,freq,date,done)
        VALUES(?,?,?,?,?,?,?) '''
		cur = self.conn.cursor()
		cur.execute(sql, (title, day, hour, minute, freq, date, done))
		self.conn.commit()
		logger.debug(cur.lastrowid)
		return cur.lastrowid
		

	def close(self):
		if self.conn:
			self.conn.close()
			logger.info("database closed")
