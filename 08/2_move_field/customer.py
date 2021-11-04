from dateutil.utils	import datetime
from units			import Amount
from contracts		import Customer as Contract

class Customer:
	_discount_rate: int;
	def __init__(self, name, discount_rate):
		self._name =			name;
		self._contract = 		Contract(datetime.now(), discount_rate);

	@property
	def discount_rate(self):
		return (self._contract._discount_rate);

	@discount_rate.setter
	def discount_rate(self, v):
		raise AttributeError("value cannot be changed manually");

	def become_preferred(self):
		self._contract._discount_rate += 0.03;

	def apply_discount(self, amount):
		amount.subtract(amount.multiply(self._contract._discount_rate));

if __name__ == "__main__":
	c = Customer("junehan", 0.2);
	print(c._contract._startdate);
	amount = Amount("customer", 10000, 100);
	print(amount);
	c.become_preferred();
	c.become_preferred();
	c.apply_discount(amount);
	print(amount);

