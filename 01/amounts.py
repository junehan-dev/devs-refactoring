def amount_for(aPerformance, play):
	"""Returns cost of aPerformanceormanced unit
		Arguments:
			aPerformance
				pref of userdata {name, audience}
			play 
				meta data of aPerformanceormace 

		Exceptions:
			ValueError
				case when play is invalid
	"""
	result = 0;
	if (play["type"] == "tragedy"):	
		result += 40000;
		if (aPerformance["audience"] > 30):
			result += 1000 * (aPerformance["audience"] - 30);
	elif (play["type"] == "comedy"):
		result += 30000;
		if (aPerformance["audience"] > 20):
			result += (1000 + 500 * (aPerformance["audience"] - 20));
		result += 300 * aPerformance["audience"];
	else:
		raise ValueError(f"Unknown genre: {play['type']}");
	return (result);
