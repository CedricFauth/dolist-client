
import re

class Dataparser():

	days_to_int = {"mon" : 0, "tue" : 1, "wed" : 2, "thu" : 3,
		"fri" : 4, "sat" : 5, "sun" : 6 }

	@staticmethod
	def parse_task(title, day, time, freq):
		day = Dataparser.days_to_int[day]
		t = time.split(':')
		return (title, day, int(t[0]), int(t[1]), freq)
		
	@staticmethod
	def parse_event(title, day, timeFromTo, freq):
		day = Dataparser.days_to_int[day]
		t = timeFromTo.split('-')
		t1 = t[0].split(':')
		t2 = t[1].split(':')

		return (title, day, t1[0], t1[1], t2[0], t2[1], freq)

	@staticmethod
	def validate(args):

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
