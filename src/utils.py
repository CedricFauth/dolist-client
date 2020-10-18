
class Color:
	BLACK = "\u001b[30m"
	RED = "\u001b[31m"
	GREEN = "\u001b[32m"
	YELLOW = "\u001b[33m"
	BLUE = "\u001b[34m"
	MAGENTA = "\u001b[35m"
	CYAN = "\u001b[36m"
	WHITE = "\u001b[37m"

	BYELLOW = "\u001b[33;1m"

	RESET = "\u001b[0m"

TODOS = [{
	"name": "Homework Computer Science",
	"due": "WE 20:52",
	"left": "2d11h"
},{
	"name": "Preparing next Lecture",
	"due": "FR 09:13",
	"left": "5d9h"
}]


class Output:

	@staticmethod
	def todos():
		"""
		prints all todos
		"""
		for entry in TODOS:
			print(f"{Color.RED}[ ]{Color.WHITE} {entry['name']}\t{entry['due']} {Color.BYELLOW}({entry['left']}){Color.RESET}")
		
