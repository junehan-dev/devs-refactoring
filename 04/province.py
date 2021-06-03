from producer import Producer
from collections import namedtuple

class Province:
	def __init__(self, doc):
		self._name = doc.name;
		self._producers = ();
		self._total_production = 0;
		self._demand = doc.demand;
		self._price = doc.price;
		[self.add_producer(Producer(self, pd)) for pd in doc.producers]

	@property
	def name(self):
		return (self._name);
	@property
	def producers(self):
		return (self._producers[:]);
	@property
	def total_production(self):
		return (self._total_production);
	@total_production.setter
	def total_production(self, v):
		self._total_production = v;
	@property
	def demand(self):
		return (self._demand);
	@demand.setter
	def demand(self, v):
		self._demand = int(v);
	@property
	def price(self):
		return (self._price);
	@price.setter
	def price(self, v):
		self._price = int(v);
	@property
	def satisfied_demand(self):
		return min((self.demand, self.total_production));
	@property
	def demand_value(self):
		return (self.satisfied_demand * self.price);
	@property
	def shortfall(self):
		return (self.demand - self.total_production);
	@property
	def demand_cost(self):
		remain = self.demand;
		def set_remain(pd):
			nonlocal remain
			ret = (pd.production if (pd.production < remain) else self.demand);
			remain -= ret;
			return (ret * pd.cost);

		contributions = map(set_remain, self.producers);
		return (sum(contributions));
	@property
	def profit(self):
		return (self.demand_value - self.demand_cost);

	def add_producer(self, producer):
		self._producers = ((producer,) + self._producers);
		self.total_production += producer.production;

def gen_province(name, producers, demand, price):
	province = namedtuple(
		'province_data',
		("name", "producers", "demand", "price")
	);
	return (province(name, producers, demand, price));

def gen_producer(name, cost, production):
	producer = namedtuple(
		'producer_data',
		("name", "cost", "production")
	);
	return (producer(name, cost, production));


def get_sample_province():
	producers = (
		gen_producer(
			name = "Byzantium", cost = 10, production = 9
		), gen_producer(
			name = "Attalia", cost = 12, production = 10
		), gen_producer(
			name = "Sinope", cost = 10, production = 6
		),
	);

	ret = gen_province(
		name = "Asia",
		producers = producers,
		demand = 30,
		price = 20,
	);

	return (ret);

