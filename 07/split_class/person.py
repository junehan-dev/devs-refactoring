from telephone import TelephoneNumber

class Person:
	def __init__(self, n, o_code, o_num):
		self._name				= n;
		self._telephone_number	= TelephoneNumber(o_code, o_num);

	@property
	def name(self):
		return (self._name);
	@name.setter
	def name(self, v):
		self._name = v;
	
	@property
	def telephone_number(self):
		return (self._telephone_number);

	@property
	def office_areacode(self):
		return (self.telephone_number.areacode);

	@office_areacode.setter
	def office_areacode(self, v):
		self.telephone_number.areacode = v;

	@property
	def office_number(self):
		return (self.telephone_number.number);

	@office_number.setter
	def office_number(self, v):
		self.telephone_number.number = v;

if	__name__ == "__main__":
	p = Person("June han", "32A", "23-142-4423");
	print(p.name,p.telephone_number);

