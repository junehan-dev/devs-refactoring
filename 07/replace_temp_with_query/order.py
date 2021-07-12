from item import Item

class Order:
	def __init__(self, q: int, i: Item):
		self._quantity = q;
		self._item = i;

	@property
	def base_price(self) -> int:
		return (self._quantity * self._item.price);

	@property
	def discount_factor(self) -> int:
		discount_factor = 0.98;
		return ((discount_factor - 0.03) if (self.base_price > 1000) else discount_factor);

	@property
	def price(self) -> int:
		return (self.base_price * self.discount_factor);

if __name__ == "__main__":
	item = Item(3000, "toy");
	a_order = Order(30, item);

	print(a_order.price);
