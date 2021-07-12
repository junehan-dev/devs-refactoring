class Order:
	def __init__(self, q, i):
		self._quantity = q;
		self._item = i;

	@property
	def price(self):
		base_price = self._quantity * self._item.price;
		discount_factor = 0.98;
		discount_factor = (discount_factor - 0.03) if (base_price > 1000) else discount_factor;
		return (base_price * discount_factor);
