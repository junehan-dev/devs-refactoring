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

	@telephone_number.setter
	def telephone_number(self, v: TelephoneNumber):
		assert(isinstance(v, TelephoneNumber) == True);
		self._telephone_number = v;

	@property
	def office_areacode(self):
		return (self.telephone_number.areacode);

	@office_areacode.setter
	def office_areacode(self, o_code):
		num = self.telephone_number.number;
		self._telephone_number = TelephoneNumber(o_code, num);

	@property
	def office_number(self):
		return (self.telephone_number.number);

	@office_number.setter
	def office_number(self, o_num):
		self.telephone_number.number = o_num;

if	__name__ == "__main__":
	p = Person("June han", "32A", "23-142-4423");
	print(p.name,p.telephone_number);
	p.office_areacode = "42B";
	print(p.name, p.telephone_number);
	p.office_number = "24-523-1234";
	print(p.name, p.telephone_number);

