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

import re

class Dataparser():

	days_to_int = {"mon" : 0, "tue" : 1, "wed" : 2, "thu" : 3,
		"fri" : 4, "sat" : 5, "sun" : 6 }

	@staticmethod
	def validate(args):
		'''
		validates input values of the user
		'''
		if not re.match('^(w|weekly|d|daily|o|once)$', args.f):
			print(f'ERROR: wrong frequency format {args.f}')
			return False
		if not re.match('^(mon|tue|wed|thur|fri|sat|sun)$', args.d):
			print(f'ERROR: wrong day format {args.d}')
			return False
		if args.cmd == 'event':
			if not re.match('^(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]-(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', args.t):
				print(f'ERROR: wrong time format {args.t}')
				return False
		else:
			if not re.match('^(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', args.t):
				print(f'ERROR: wrong time format {args.t}')
				return False
		return True

	@staticmethod
	def parse_event(title, day, timeFromTo, freq):
		'''
		event data gets prepared for database
		'''
		day = Dataparser.days_to_int[day]
		t = timeFromTo.split('-')
		t1 = t[0].split(':')
		t2 = t[1].split(':')
		return (title, day, t1[0], t1[1], t2[0], t2[1], freq, )

	@staticmethod
	def parse_task(title, day, time, freq):
		'''
		task data gets prepared for database
		'''
		day = Dataparser.days_to_int[day]
		t = time.split(':')
		return (title, day, int(t[0]), int(t[1]), freq, )
