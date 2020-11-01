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

	def show_overview(self):
		logger.info('cmd: show overview')
		data = self.db.get_overview_data()
		raise NotImplementedError
		# DEBUG TODO remove
		logger.debug("Events today")
		for r in data[0]:
			logger.debug(r)
		logger.debug("All tasks")
		for r in data[1]:
			logger.debug(r)
		# TODO process data
		# TODO implement output

	def add_event(self, title, day, timeFromTo, freq):
		logger.info('cmd: event')
		if freq[0] == 'w':
			args = Dataparser.parse_event(title, day, timeFromTo, freq)
			self.db.new_event(*args) # tupel to parameters (*) 
		else:
			# TODO implement
			raise NotImplementedError
		# TODO output message
		print("Event added.")

	def add_task(self, title, day, time, freq):
		if freq[0] == 'w':
			args = Dataparser.parse_task(title, day, time, freq)
			self.db.new_task(*args) # tupel to parameters (*) 
		else:
			# TODO implement
			raise NotImplementedError
		# TODO output message
		print("Task added.")

	def list_ids(self):
		logger.info(f'cmd: list_ids')
		data = self.db.get_id_list()

		# DEBUG TODO remove
		logger.debug("Event IDs")
		for r in data[0]:
			logger.debug(r)
		logger.debug("Task IDs")
		for r in data[1]:
			logger.debug(r)
		# TODO process data
		# TODO implement output

	def remove_by_id(self, id, typ):
		logger.info(f'cmd: remove_by_id -{typ} {id}')
		self.db.delete_data(id, typ)

	def exit(self):
		self.db.close()


def main():
	# parse cli
	p = CLI_Parser()

	if not Dataparser.validate(p.args):
		return 0

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
	
	c.exit()

	return 0
	

if __name__ == '__main__':
	main()
