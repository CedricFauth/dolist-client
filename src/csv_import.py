import csv
from dolist import Controller
import sys
from cli import Output

def main():
	c = Controller()
	if len(sys.argv) != 2:
		Output.error("usage: dlimport [filename]")
		c.exit()
		return 0
	try:
		csvfile = open(sys.argv[1], newline='', encoding='utf-8-sig')
		reader = csv.reader(csvfile, delimiter=';')
		category = ''
		for row in reader:
			if row[0] == 'events':
				category = 'e'
				continue
			elif row[0] == 'tasks':
				category = 't'
				continue
			elif row[0] == '':
				continue

			if category == 'e':
				pass
				print(row[0], row[2], f'{row[3]}-{row[4]}', row[1])
				c.add_event(row[0], row[2], f'{row[3]}-{row[4]}', row[1])
			elif category == 't':
				print(row[0], row[2], row[3], row[1])
				c.add_task(row[0], row[2], row[3], row[1])
		csvfile.close()
	except FileNotFoundError:
		Output.error("file not found")
	finally:
		c.exit()

if __name__ == '__main__':
	main()
