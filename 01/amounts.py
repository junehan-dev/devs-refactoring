def amount_for(aPerformance):
	"""Returns cost of aPerformanceormanced unit
		Arguments:
			aPerformance
				perf of copied userdata {name, audience}

		Exceptions:
			ValueError
				case when play is invalid
	"""
	result = 0;
	if (aPerformance["play"]["type"] == "tragedy"):	
		result += 40000;
		if (aPerformance["audience"] > 30):
			result += 1000 * (aPerformance["audience"] - 30);
	elif (aPerformance["play"]["type"] == "comedy"):
		result += 30000;
		if (aPerformance["audience"] > 20):
			result += (1000 + 500 * (aPerformance["audience"] - 20));
		result += 300 * aPerformance["audience"];
	else:
		raise ValueError(f"Unknown genre: {aPerformance['play']['type']}");
	return (result);
