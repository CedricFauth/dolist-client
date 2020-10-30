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
		self.e_parser.add_argument('-d', type=str, action='store', required=True, help='weekday')
		self.e_parser.add_argument('-t', type=str, action='store', required=True, help='time period HH:MM-HH:MM')
		self.e_parser.add_argument('-f', type=str, action='store', required=True, help='frequency')
		# task args
		self.t_parser = self.subparsers.add_parser('task', help='add a task (task -h)')
		self.t_parser.add_argument('title', type=str, action='store', help='task title')
		self.t_parser.add_argument('-d', type=str, action='store', required=True, help='weekday')
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
		# other args
		#self.group = self.parser.add_mutually_exclusive_group()
		#self.group.add_argument('-le', action='store_true', help='list events')
		#self.group.add_argument('-lt', action='store_true', help='list tasks')
		#self.group.add_argument('-re', type=int, action='store', help='remove events')
		#self.group.add_argument('-rt', type=int, action='store', help='remove tasks')
		# parse
		self.args = self.parser.parse_args()
		logger.debug(self.args)
