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

from parser import CLI_Parser
from database import Database
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def main():
	p = CLI_Parser()
	
	if p.args.cmd and (p.args.le or p.args.lt or p.args.re or p.args.rt):
		print(f"You cannot use {p.args.cmd} here.")
		return 0
	
	d = Database()
	d.close()
	if p.args.cmd == 'event':
		logger.info('cmd: event')
	elif p.args.cmd == 'task':
		logger.info('cmd: task')
	elif p.args.le:
		logger.info("cmd: le")
	elif p.args.lt:
		logger.info("cmd: lt")
	elif p.args.re:
		logger.info(f'cmd: re {p.args.re}')
	elif p.args.rt:
		logger.info(f'cmd: rt {p.args.rt}')
	else:
		logger.info('cmd: showing overview')
	
	return 0
	

if __name__ == '__main__':
	main()
