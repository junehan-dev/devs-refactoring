from dataclasses import dataclass

@dataclass(frozen = False)
class TelephoneNumber:
	_areacode: str;

	@property
	def areacode(self):
		return (self._areacode);

	@areacode.setter
	def areacode(self, v):
		self._areacode = v;

	def __str__(self):
		return (self.areacode + " is number");

