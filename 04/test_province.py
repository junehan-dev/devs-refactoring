import unittest
from functools import reduce
from province import Province, get_sample_province

class ProvinceTestCase(unittest.TestCase):
	def test_total_production(self):
		"""test getter.total_production
		"""
		asia = Province(get_sample_province());
		total = reduce(lambda a, b: a + b.production, asia.producers, 0);
		self.assertEqual(asia.total_production, total);

	def test_shotfall(self):
		"""test getter.shortfall
		"""
		asia = Province(get_sample_province());
		self.assertEqual(asia.shortfall, 5);

if __name__ == "__main__":
	unittest.main();
