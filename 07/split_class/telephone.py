from dataclasses import dataclass

@dataclass(frozen = False)
class TelephoneNumber:
	_areacode: str;
	_number: str;

	@property
	def areacode(self):
		return (self._areacode);

	@areacode.setter
	def areacode(self, v):
		self._areacode = v;

	@property
	def number(self):
		return (self._number);

	@number.setter
	def number(self, v):
		self._number = v;

	def __str__(self):
		return (f"{self.areacode} {self.number}");

