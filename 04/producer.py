class Producer:
	def __init__(self, aProvince, data):
		self._name = data.name;
		self._cost = data.cost;
		self._province = aProvince;
		self._production = (data.production if data.production else 0);

	@property
	def name(self):
		return (self._name);
	@property
	def cost(self):
		return (self._cost);
	@cost.setter
	def cost(self, v):
		self._cost = v;
	@property
	def production(self):
		return (self._production);
	@production.setter
	def production(self, v):
		amount = int(v);
		new_prod = (amount if amount else 0);
		self._province.total_production += (new_prod - self._production);
		self._production = new_prod;

