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

	@staticmethod
	def open():
		print(sym.default(), end='', flush=True)
	
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
	
	@staticmethod
	def list_all(events, tasks):
		out = f'{sym.CYAN}event [ID]  [TITLE]{"".join(" " for _ in range(49))}'
		out += f'[FROM - TO]{sym.default()}'
		le = len(events) - 1
		lt = len(tasks) - 1
		for i,e in enumerate(events):
			title = Output.process_title(e[1], 55)
			if i == le:
				out += f'\n{sym.BOX2}{sym.BOX3*4}'
			else:
				out += f'\n{sym.BOX1}{sym.BOX3*4}' 
			out += f' {"{:<3}".format(e[0])}   {title} {e[3]}-{e[4]}'
		out += f'\n{sym.MAGENTA}task  [ID]  [TITLE]{"".join(" " for _ in range(55))}'
		out += f'[DUE]{sym.default()}'
		for i,t in enumerate(tasks):
			title = Output.process_title(t[1], 61)
			if i == lt:
				out += f'\n{sym.BOX2}{sym.BOX3*4}'
			else:
				out += f'\n{sym.BOX1}{sym.BOX3*4}' 
			out += f' {"{:<3}".format(t[0])}   {title} {t[3]}'
		out += sym.default()
		print(out)

	@staticmethod
	def process_title(title, max_len):
		"""
		shortens or extends a title to max_len
		"""
		if len(title) > max_len:
			return title[:max_len - 3] + '...'
		else:
			return title + ''.join(' ' for _ in range(max_len-len(title)))

		

