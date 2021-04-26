from abc import ABCMeta, abstractmethod


class PerformanceCalculator(metaclass = ABCMeta):
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
		return (max((self.audience - 30, 0)));

	@abstractmethod
	def _amount(self):
		"""Returns cost of aPerformanceormanced unit
			Exceptions:
				ValueError
					case when play is invalid
		"""

	@property
	def amount(self):
		return self._amount();

class ComedyCalculator(PerformanceCalculator):
	def __init__(self, aPerf, play):
		super().__init__(aPerf, play);

	def _amount(self):
		result = 30000;
		if (self.audience > 20):
			result += (1000 + 500 * (self.audience - 20));
		result += 300 * self.audience;
		return (result);

	@property
	def volume_credit(self):
		return super().volume_credit + int(self.audience/5);


class TragedyCalculator(PerformanceCalculator):
	def __init__(self, aPerf, play):
		super().__init__(aPerf, play);

	def _amount(self):
		result = 40000;
		if (self.audience > 30):
			result += 1000 * (self.audience - 30);
		return (result);
