from dataclasses import dataclass

@dataclass(frozen = False)
class TelephoneNumber:
	_office_areacode: str;

	@property
	def office_areacode(self):
		return (self._office_areacode);

	@office_areacode.setter
	def office_areacode(self, v):
		self._office_areacode = v;

	def __str__(self):
		return (self.office_areacode + " is number");

