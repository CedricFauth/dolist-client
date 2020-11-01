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

def striken(text):
	return ''.join(t+chr(822) for t in text)

class Color:
	BLACK = "\u001b[30m"
	RED = "\u001b[31m"
	GREEN = "\u001b[32m"
	YELLOW = "\u001b[33m"
	BLUE = "\u001b[34m"
	MAGENTA = "\u001b[35m"
	CYAN = "\u001b[36m"
	WHITE = "\u001b[37m"

	BRED = "\u001b[31;1m"
	BYELLOW = "\u001b[33;1m"
	BBLUE = "\u001b[34;1m"

	BACKBLUE = "\u001b[44m"

	DIM = "\u001b[2m"

	RESET = "\u001b[0m"

	@staticmethod
	def default():
		return "\u001b[0m\u001b[37m"

#print(f"{Color.default()}\n1:\n")

#print(Color.default() + f"\u256D\u2500\u2500( \u001b[1mToday's events{Color.default()} )"+"".join("\u2500" for _ in range(0,58))+"\u256E")
#print(f"\u2502{Color.BLUE} \u25B6{Color.default()} Lecture Human Computer Interaction\t\t\tTUE 10:00 {Color.CYAN}(1h 13m){Color.default()}     \u2502")
#print(f"\u2502{Color.WHITE} \u25B6 Exercise Human Computer Interaction\t\t\tTUE 11:30 (2h 43m){Color.default()}     \u2502")
#print(f"\u251C\u2500\u2500( \u001b[1mThis week's assignments{Color.default()} )" + "".join("\u2500" for _ in range(0,49))+"\u2524")
#print(f"\u2502{Color.RED}[ ]{Color.WHITE} IT Security Assignment 01\t\t\t\tMON 23:55 {Color.RED}(22h 40m){Color.default()}    \u2502")
#print(f"\u2502{Color.RED}[ ]{Color.WHITE} Human Computer Interaction Assignment 02\t\tMON 23:55 {Color.BYELLOW}(1d 22h 40m){Color.default()} \u2502")
#print(f"\u2502{Color.GREEN}[\u2714]{Color.WHITE} {striken('Proseminar Preperation')}\t\t\t\t\u001b[42m{Color.default()}{striken('MON 23:55 (1d 22h 40m)')}{Color.default()} \u2502")
#print("\u2570" + "".join("\u2500" for _ in range(0,78)) + "\u256F")

print(f"{Color.default()}\033[2J\033[H\nLayout:\n")

print(Color.default() + f"{Color.CYAN}\u2500\u2500\u2500[ \u001b[1mToday's events{Color.default()}{Color.CYAN} ]"+"".join("\u2500" for _ in range(0,59)))
print(f"{Color.BLUE} \u25B6{Color.default()} Lecture Human Computer Interaction\t\t      [w] 10:00-11:30   (1h13m){Color.default()}")
print(f"{Color.BLUE} \u25B6{Color.default()} {Color.DIM}Exercise Human Computer Interaction\t\t      [w] 11:30-13:00   (2h43m){Color.default()}")
print(f"{Color.BLUE} \u25B6{Color.default()} {Color.DIM}Foundations of Information Retrieval\t\t      [w] 14:00-15:00  (13h13m){Color.default()}")

print(Color.default() + f"{Color.MAGENTA}\u2500\u2500\u2500[ \u001b[1mAssignments{Color.default()}{Color.MAGENTA} ]"+"".join("\u2500" for _ in range(0,62)))
print(f"{Color.RED} [ ]{Color.WHITE} IT Security Assignment 01\t\t\t      [w] MON 08:15{Color.BRED}     (9h40m){Color.default()}")
print(f"{Color.RED} [ ]{Color.WHITE} Human Computer Interaction Assignment 02\t      [w] MON 23:55{Color.BYELLOW}  (1d22h40m){Color.default()}")
print(f"{Color.GREEN} [\u2714]{Color.WHITE} {striken('Proseminar Preperation')}\t\t\t      [w] \u001b[42m{Color.default()}{striken('MON 23:55  (1d22h40m)')}{Color.default()}")

print("\nInput format:\n")
print("Show today's events and all assignments:")
print(f"{Color.MAGENTA}$ >{Color.default()} dl")
print("Add an event (-e):")
print(f"{Color.MAGENTA}$ >{Color.default()} dl task 'VL Human Computer Interaction' -f w -t 15:00-16:30 -d MON")
print(f"{Color.MAGENTA}$ >{Color.default()} dl task 'VL Human Computer Interaction' -f d -t 15:00-16:30")
print(f"{Color.MAGENTA}$ >{Color.default()} dl task 'VL Human Computer Interaction' -f o -t 15:00-16:30 -d 2020-12-24")
print("Add an assignment (-a):")
print(f"{Color.MAGENTA}$ >{Color.default()} dl -a 'Homework MCI' -d FRI -t 00:00 -f once")
print("List all events and IDs:")
print(f"{Color.MAGENTA}$ >{Color.default()} dl -le")
print("List all assignments and IDs:")
print(f"{Color.MAGENTA}$ >{Color.default()} dl -la")
print("Remove event:")
print(f"{Color.MAGENTA}$ >{Color.default()} dl -re ID")
print("Remove event:")
print(f"{Color.MAGENTA}$ >{Color.default()} dl -ra ID")
print()
