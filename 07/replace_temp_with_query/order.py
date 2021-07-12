from item import Item

class Order:
	def __init__(self, q: int, i: Item):
		self._quantity = q;
		self._item = i;

	@property
	def base_price(self) -> int:
		base_price = self._quantity * self._item.price;
		return (base_price);

	@property
	def discount_factor(self) -> int:
		discount_factor = 0.98;
		return ((discount_factor - 0.03) if (self.base_price > 1000) else discount_factor);

	@property
	def price(self) -> int:
		BASE_PRICE = self.base_price;
		DISCOUNT_FACTOR = self.discount_factor;
		return (BASE_PRICE * DISCOUNT_FACTOR);

if __name__ == "__main__":
	item = Item(3000, "toy");
	a_order = Order(30, item);

	print(a_order.price);
