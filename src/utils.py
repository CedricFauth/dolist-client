
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
	def reset():
		return "\u001b[0m\u001b[37m"

	@staticmethod
	def striken(text):
		return ''.join(t+chr(822) for t in text)
