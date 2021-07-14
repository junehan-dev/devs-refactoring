from telephone import TelephoneNumber

class Person:
	def __init__(self, n, o_code, o_num):
		self._name				= n;
		self._office_number		= o_num;
		self._telephone_number	= TelephoneNumber(o_code);

	@property
	def name(self):
		return (self._name);
	@name.setter
	def name(self, v):
		self._name = v;
	
	@property
	def office_areacode(self):
		return (self.telephone_number.areacode);

	@office_areacode.setter
	def office_areacode(self, v):
		self.telephon_number.areacode = v;

	@property
	def office_number(self):
		return (self._office_number);

	@office_number.setter
	def office_number(self, v):
		self._office_number = v;

	@property
	def telephone_number(self):
		return (self._telephone_number);

if	__name__ == "__main__":
	p = Person("June han", "32A", "23-142-4423");
	print(p.name, p.office_areacode, p.office_number, p.telephone_number);

