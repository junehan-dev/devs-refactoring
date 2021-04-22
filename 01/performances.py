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

	@property
	def volume_credit(self):
		result = max((self.audience - 30, 0));
		if (self.play["type"] == "comedy"):
			result += int(self.audience / 5);
		return (result);

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

