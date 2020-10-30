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

from cli import CLI_Parser
from database import Database
from data import Dataparser
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Controller:
	def __init__(self):
		self.db = Database()
		self.intdays = {"mon" : 0, "tue" : 1, "wed" : 2, "thu" : 3,
		"fri" : 4, "sat" : 5, "sun" : 6 }

	def show_overview(self):
		logger.info('cmd: show overview')
		raise NotImplementedError

	def add_event(self, title, day, timeFromTo, freq):
		logger.info('cmd: event')
		if freq == 'w':
			t = timeFromTo.split('-')
			t1 = t[0].split(':')
			t2 = t[1].split(':')
			self.db.new_event(title, self.intdays[day], t1[0], t1[1], t2[0], t2[1], freq)
		else:
			raise NotImplementedError

	def add_task(self, title, day, time, freq):
		logger.info('cmd: task')
		if freq == 'w':
			t = time.split(':')
			self.db.new_task(title, self.intdays[day], t[0], t[1], freq)
		else:
			raise NotImplementedError

	def list_ids(self):
		logger.info(f'cmd: list_ids')
		raise NotImplementedError

	def remove_by_id(self, id, typ):
		logger.info(f'cmd: remove_by_id -{typ} {id}')
		raise NotImplementedError

	def exit(self):
		self.db.close()

def main():
	p = CLI_Parser()

	#if p.args.cmd and (p.args.le or p.args.lt or p.args.re or p.args.rt):
	#	print(f"You cannot use {p.args.cmd} here.")
	#	return 0
	
	c = Controller()

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
	else:
		print("Error: Unknown Error - Please report.")
	
	c.exit()

	return 0
	

if __name__ == '__main__':
	main()
