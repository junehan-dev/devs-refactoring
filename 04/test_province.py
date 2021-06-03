import unittest
from functools import reduce
from province import Province, get_sample_province

class ProvinceTestCase(unittest.TestCase):
	def setUp(self):
		self.asia = Province(get_sample_province());

	def test_total_production(self):
		"""test getter.total_production
		"""
		total = reduce(lambda a, b: a + b.production, self.asia.producers, 0);
		self.assertEqual(self.asia.total_production, total);

	def test_shotfall(self):
		"""test getter.shortfall
		"""
		self.assertEqual(self.asia.shortfall, 5);

if __name__ == "__main__":
	unittest.main();
