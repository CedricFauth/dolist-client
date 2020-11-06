'''
MIT License

Copyright (c) 2020 Cedric Fauth

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sqlite3
from os import path
from datetime import datetime, date
import logging
import os


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.ERROR)

class Database:
	def __init__(self):
		self.dirname = os.path.dirname(__file__)
		self.path = os.path.join(self.dirname[:-3], 'data.db')
		#self.path = "./data.db"
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
			day integer,
			start_time text NOT NULL,
			end_time text NOT NULL,
			freq text NOT NULL,
			date text
			); """
		create_task_table = """ CREATE TABLE tasks (
			id integer PRIMARY KEY autoincrement,
			title text NOT NULL,
			day integer,
			time text NOT NULL,
			freq text NOT NULL,
			date text,
			done integer,
			done_on text
			); """
		try:
			c = self.conn.cursor()
			c.execute(create_event_table)
			c.execute(create_task_table)
		except Exception as e:
			logging.ERROR(e)

	def new_event(self,title,day,s_time,e_time,freq,date):
		sql = ''' INSERT INTO events 
		(title,day,start_time,end_time,freq,date)
        VALUES(?,?,?,?,?,?); '''
		cur = self.conn.cursor()
		cur.execute(sql, (title,day,s_time,e_time,freq,date,))
		self.conn.commit()
		logger.info(f'inserted: {cur.lastrowid}')
		return cur.lastrowid

	def new_task(self,title,day,time,freq,date,done_on=None,done=0):
		sql = ''' INSERT INTO tasks 
		(title,day,time,freq,date,done,done_on)
        VALUES(?,?,?,?,?,?,?); '''
		cur = self.conn.cursor()
		cur.execute(sql, (title,day,time,freq,date,done,done_on,))
		self.conn.commit()
		logger.info(f'inserted: {cur.lastrowid}')
		return cur.lastrowid
	
	def get_overview_data(self):

		today = date.today()
		weekday = today.weekday()

		sql1 = '''SELECT * FROM events
		WHERE (day = ? AND freq = 'w') OR (date = ?) OR (freq = 'd')
		ORDER BY start_time ASC;'''
		sql2 = '''SELECT * FROM tasks
		WHERE done = ?;'''

		cur = self.conn.cursor()
		cur.execute(sql1, (weekday, today.isoformat()))
		event_rows = cur.fetchall()
		cur.execute(sql2, (0, ))
		task_rows_todo = cur.fetchall()
		cur.execute(sql2, (1, ))
		task_rows_done = cur.fetchall()

		return (event_rows, task_rows_todo, task_rows_done)

	def get_done_tasks(self):
		sql1 = '''SELECT * FROM tasks
		WHERE done = 1;'''
		cur = self.conn.cursor()
		cur.execute(sql1)
		task_rows_done = cur.fetchall()
		return task_rows_done
		
	def get_id_list(self):
		sql1 = '''SELECT * FROM events;'''
		sql2 = '''SELECT * FROM tasks;'''

		cur = self.conn.cursor()
		cur.execute(sql1)
		event_rows = cur.fetchall()
		cur.execute(sql2)
		task_rows = cur.fetchall()

		return (event_rows, task_rows, )

	def delete_data(self, id, typ):
		sql1 = 'DELETE FROM events WHERE id=? ;'
		sql2 = 'DELETE FROM tasks WHERE id=? ;'
		cur = self.conn.cursor()
		if typ == 'e':
			cur.execute(sql1, (id, ))
		else:
			cur.execute(sql2, (id, ))
		self.conn.commit()

	def get_task_by(self, id):
		sql1 = '''SELECT * FROM tasks WHERE id = ?;'''
		cur = self.conn.cursor()
		cur.execute(sql1, (id, ))
		return cur.fetchone()

	def set_done(self, task_id, date):
		sql1 = '''update tasks set done_on = ?,
		done=1 where id = ?;'''
		cur = self.conn.cursor()
		cur.execute(sql1, (date, task_id, ))
		self.conn.commit()
		logger.info(f'updated: done=1 and done-date="{date}" at id {task_id}')

	def reset_done(self, reset_id_list):
		sql1 = '''UPDATE tasks SET done = 0 WHERE id = ?;'''
		sql2 = '''DELETE FROM tasks WHERE id = ?;'''
		cur = self.conn.cursor()
		logger.info(reset_id_list)
		for id,freq in reset_id_list:
			if freq == 'o': 
				cur.execute(sql2, (id, ))
			else: 
				cur.execute(sql1, (id, ))
			logger.info(f'reset: done=0 at id {id}')
		self.conn.commit()

	def close(self):
		if self.conn:
			self.conn.close()
			logger.info("database closed")
