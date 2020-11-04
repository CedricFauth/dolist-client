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

from cli import CLI_Parser, Output as Out
from database import Database
from data import Dataparser
import logging
from datetime import date, datetime

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Controller:
	def __init__(self):
		Out.open()
		self.db = Database()

	def reset_done_tasks(self):
		data = self.db.get_done_tasks()
		reset_id_list = Dataparser.get_reset_ids(data)
		self.db.reset_done(reset_id_list)
	
	# TODO implement 'done' and set done_on (duedate + duetime)

	def show_overview(self):
		logger.info('cmd: show overview')
		# TODO process_events
		data = self.db.get_overview_data()
		e = Dataparser.prepare_out_events(data[0])
		t = Dataparser.prepare_out_tasks(data[1])
		td = Dataparser.prepare_out_tasks(data[2])
		
		for i in t:
			print(i)
		print()
		for i in td:
			print(i)
		Out.overview(e, t, td)
		# TODO implement 'done'

	def add_event(self, title, day, timeFromTo, freq):
		logger.info('cmd: event')

		args = Dataparser.parse('e', title, day, timeFromTo, freq)
		self.db.new_event(*args) # tupel to parameters (*) 

		Out.info("event added")

	def add_task(self, title, day, time, freq):
		logger.info('cmd: task')
		args = Dataparser.parse('t', title, day, time, freq)
		self.db.new_task(*args) # tupel to parameters (*) 
		Out.info("task added")

	def list_ids(self):
		logger.info(f'cmd: list_ids')
		data = self.db.get_id_list()
		Out.list_all(data[0], data[1])

	def remove_by_id(self, id, typ):
		logger.info(f'cmd: remove_by_id -{typ} {id}')
		self.db.delete_data(id, typ)
		if typ == 't':
			Out.info(f"task {id} deleted")
		elif typ == 'e':
			Out.info(f"event {id} deleted")

	def done(self, id):
		# TODO implement
		t = self.db.get_task_by(id)
		print(t)
		if not t:
			Out.error(f'no task with id {id} found')
			return 0
		
		if t[4] == 'w':
			done_time = Dataparser.nearest_deadline(t)
			print(done_time)
			self.db.set_done(id, done_time)
		#	# find date of weekday t[w] that is >= (after/eq) t[3]
		#	done_time = f'{Dataparser.date_of_nearest_weekday(done_datetime, t[3])} {t[3]}'
		#	logger.info(f'set done {id} with done-date "{done_time}"')
		#	
		else: raise NotImplementedError

	def exit(self):
		self.db.close()
		Out.close()


def main():
	# parse cli
	p = CLI_Parser()

	if not Dataparser.validate(p.args):
		return 0

	c = Controller()
	#c.reset_done_tasks()

	if p.args.cmd == None:
		c.show_overview()
	elif p.args.cmd == 'event':
		c.add_event(p.args.title, p.args.d, p.args.t, p.args.f)
	elif p.args.cmd == 'task':
		c.add_task(p.args.title, p.args.d, p.args.t, p.args.f)
	elif p.args.cmd == 'rm' and p.args.t:
		c.remove_by_id(p.args.id, 't')
	elif p.args.cmd == 'rm' and p.args.e:
		c.remove_by_id(p.args.id, 'e')
	elif p.args.cmd == 'ls':
		c.list_ids()
	elif p.args.cmd == 'done':
		c.done(p.args.task_id)
	
	c.exit()

	return 0
	

if __name__ == '__main__':
	main()
