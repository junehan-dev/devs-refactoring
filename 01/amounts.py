def amount_for(perf, play):
	"""Returns cost of performanced unit
		Arguments:
			pref
				performance of userdata {name, audience}
			play 
				meta data of performace 

		Exceptions:
			ValueError
				case when play is invalid
	"""
	this_amount = 0;
	if (play["type"] == "tragedy"):	
		this_amount += 40000;
		if (perf["audience"] > 30):
			this_amount += 1000 * (perf["audience"] - 30);
	elif (play["type"] == "comedy"):
		this_amount += 30000;
		if (perf["audience"] > 20):
			this_amount += (1000 + 500 * (perf["audience"] - 20));
		this_amount += 300 * perf["audience"];
	else:
		raise ValueError(f"Unknown genre: {play['type']}");
	return (this_amount);
