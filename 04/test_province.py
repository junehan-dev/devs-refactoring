import unittest
from functools import reduce
from province import Province, get_sample_province

class ProvinceTestCase(unittest.TestCase):
	def setUp(self):
		self.asia = Province(get_sample_province());

	def	test_diff_prod_to_profit(self):
		self.asia.producers[0].production = 20;
		self.assertEqual(self.asia.profit, -260);

	def test_diff_prod_to_shortfall(self):
		self.asia.producers[0].production = 20;
		self.assertEqual(self.asia.shortfall, self.asia.demand - self.asia.total_production);

	def test_profit(self):
		self.assertEqual(self.asia.profit, 230);

	def test_total_production(self):
		"""test getter.total_production
		"""
		total = reduce(lambda a, b: a + b.production, self.asia.producers, 0);
		self.assertEqual(self.asia.total_production, total);

	def test_shotfall(self):
		"""test getter.shortfall
		"""
		self.assertEqual(self.asia.shortfall, 5);

from province import gen_producer, gen_province
class ProvinceNegativeTestCase(unittest.TestCase):
	def test_no_prods(self):
		desert_data = gen_province("desert", [], 30, 20);
		desert = Province(desert_data);
		self.assertEqual(desert.shortfall, 30);
		desert.demand = 0;
		self.assertEqual(desert.shortfall, -25);
		self.assertEqual(desert.profit, 0);
		self.assertEqual(desert.demand, 0);
		
if __name__ == "__main__":
	unittest.main();
