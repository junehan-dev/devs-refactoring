from random import choice

class Order:
	_priority: str;
	_id: int = 0;

	def __init__(self, d:str):
		self._priority = d;
		self.id = Order.get_id();
	
	@property
	def priority(self):
		return (self._priority);

	@priority.setter
	def priority(self, new_priority):
		self._priority = new_priority;

	def __str__(self):
		return f"{self.id}: {self.priority}";

	@classmethod
	def get_id(cls):
		temp = cls._id;
		cls._id += 1;
		return (temp);

def get_high_orders():
	CHOOSABLE = ("high", "low");
	raw_datas = [choice(CHOOSABLE) for _ in range(10)];
	orders = map(Order, raw_datas);
	ret = filter(lambda o: o.priority == "high", orders);
	return (ret);
	
if __name__ == "__main__":
	high_priority_orders = get_high_orders();
	[print(h_o) for h_o in high_priority_orders];

