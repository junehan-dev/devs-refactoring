class PerformanceCalculator:
	def __init__(self, aPerformance, aPlay):
		self._performance = aPerformance;
		self._play = aPlay;
		return (None);

	@property
	def play(self):
		return (self._play);

	@property
	def performance(self):
		return (self._performance);

	@property
	def audience(self):
		return (self.performance["audience"]);

	def _amount(self):
		"""Returns cost of aPerformanceormanced unit
			Exceptions:
				ValueError
					case when play is invalid
		"""
		result = 0;
		if (self.play["type"] == "tragedy"):	
			result += 40000;
			if (self.audience > 30):
				result += 1000 * (self.audience - 30);
		elif (self.play["type"] == "comedy"):
			result += 30000;
			if (self.audience > 20):
				result += (1000 + 500 * (self.audience - 20));
			result += 300 * self.audience;
		else:
			raise ValueError(f"Unknown genre: {self.play['type']}");
		return (result);

	@property
	def amount(self):
		return self._amount();



def _amount_for(aPerformance):
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


