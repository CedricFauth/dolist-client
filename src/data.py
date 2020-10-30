
class Dataparser():

	days_to_int = {"mon" : 0, "tue" : 1, "wed" : 2, "thu" : 3,
		"fri" : 4, "sat" : 5, "sun" : 6 }

	@staticmethod
	def parse_input(day, time):
		out = {}
		out['day'] = days_to_int[day]
		t = time.split(':')
		out['hour'] = int(t[0])
		out['minute'] = int(t[1])
		return out
		

		
