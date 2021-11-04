from dataclasses	import dataclass
from datetime		import datetime

@dataclass
class Customer:
	_startdate: datetime
	_discount_rate: int;

	@property
	def discount_rate(self):
		return (self._discount_rate);	
	
	@discount_rate.setter
	def discount_rate(self, v):
		self._discount_rate = v;
		return (None);

