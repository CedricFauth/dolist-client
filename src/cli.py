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

import argparse
import logging
from utils import Symbol as sym

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class CLI_Parser:

	def __init__(self):
		# init parser
		self.parser = argparse.ArgumentParser('dolist client')
		self.subparsers = self.parser.add_subparsers(dest="cmd")
		# event args
		self.e_parser = self.subparsers.add_parser('event', help='add an event (event -h)')
		self.e_parser.add_argument('title', type=str, action='store', help='event title')
		self.e_parser.add_argument('-d', type=str, action='store', help='weekday or date')
		self.e_parser.add_argument('-t', type=str, action='store', required=True, help='time period HH:MM-HH:MM')
		self.e_parser.add_argument('-f', type=str, action='store', required=True, help='frequency')
		# task args
		self.t_parser = self.subparsers.add_parser('task', help='add a task (task -h)')
		self.t_parser.add_argument('title', type=str, action='store', help='task title')
		self.t_parser.add_argument('-d', type=str, action='store', help='weekday')
		self.t_parser.add_argument('-t', type=str, action='store', required=True, help='time HH:MM')
		self.t_parser.add_argument('-f', type=str, action='store', required=True, help='frequency')
		# remove
		self.rm_parser = self.subparsers.add_parser('rm', help='remove event or task')
		self.rm_group = self.rm_parser.add_mutually_exclusive_group(required=True)
		self.rm_group.add_argument('-e', action='store_true', help='remove event')
		self.rm_group.add_argument('-t', action='store_true', help='remove task')
		self.rm_parser.add_argument('id', type=int, action='store', help='id of event/task')
		# list
		self.ls_parser = self.subparsers.add_parser('ls', help='list all id\'s')
		
		# parse
		self.args = self.parser.parse_args()
		logger.debug(self.args)

class Output:

	int_to_days = {None: '', 0: "mon", 1: "tue", 2: "wed", 3: "thu",
		4: "fri", 5: "sat", 6: "sun"}
	
	char_to_freq = {'w': 'weekly', 'd': 'daily', 'o': 'once'}

	@staticmethod
	def open():
		# \033[2J\033[H clear screen
		print(f'{sym.default()}', end='', flush=True)
	
	@staticmethod
	def close():
		print(sym.RESET, end='', flush=True)

	@staticmethod
	def info(msg):
		"""
		prints an info text
		"""
		print(f' {sym.MAGENTA}{sym.DONE}{sym.default()} {msg}')
	
	@staticmethod
	def error(msg):
		"""
		prints an error text
		"""
		print(f' {sym.RED}{sym.ERR}{sym.default()} {msg}')
	
	# TODO SHOW ALL PARAMETERS
	@staticmethod
	def list_all(events, tasks):
		le = len(events) - 1
		lt = len(tasks) - 1
		event_head = f'{sym.CYAN}event [ID] [TITLE]{"".join(" " for _ in range(27))}' + \
			f'[FREQ] [DAY] [DATE]     [FROM - TO]{sym.default()}'
		task_head = f'\n{sym.MAGENTA}task  [ID] [TITLE]{"".join(" " for _ in range(33))}' + \
			f'[FREQ] [DAY] [DATE]     [DUE]{sym.default()}'
		out = event_head
		for i,e in enumerate(events):
			title = Output.process_text(e[1], 33)
			freq = Output.process_text(Output.char_to_freq[e[5]], 6)
			day = Output.process_text(Output.int_to_days[e[2]], 5)
			date = (e[6] if e[6] != None else '          ')
			if i == le:
				out += f'\n{sym.BOX2}{sym.BOX3*4} '
			else:
				out += f'\n{sym.BOX1}{sym.BOX3*4} ' 
			out += f'{Output.process_text(str(e[0]), 4)} {title} {freq} {day} {date} {e[3]}-{e[4]}'
		out += task_head
		for i,t in enumerate(tasks):
			title = Output.process_text(t[1], 39)
			freq = Output.process_text(Output.char_to_freq[t[4]], 6)
			day = Output.process_text(Output.int_to_days[t[2]], 5)
			date = (t[5] if t[5] != None else '          ')
			if i == lt:
				out += f'\n{sym.BOX2}{sym.BOX3*4} '
			else:
				out += f'\n{sym.BOX1}{sym.BOX3*4} ' 
			out += f'{Output.process_text(str(t[0]), 4)} {title} {freq} {day} {date} {t[3]}'
		out += sym.default()
		print(out, flush=True)

	@staticmethod
	def process_text(title, max_len):
		"""
		shortens or extends a title to max_len
		"""
		if len(title) > max_len:
			return title[:max_len - 3] + '...'
		else:
			return title + ''.join(' ' for _ in range(max_len-len(title)))

	def overview():
		pass

		

