from item import Item
class Order:
	_item	: Item;

	def __init__(self, q, i):
		self._quantity = q;
		self._item = i;

	@property
	def price(self):
		BASE_PRICE = self._quantity * self._item.price;
		discount_factor = 0.98;
		discount_factor = (discount_factor - 0.03) if (BASE_PRICE > 1000) else discount_factor;
		return (BASE_PRICE * discount_factor);

if __name__ == "__main__":
	item = Item(3000, "toy");
	a_order = Order(30, item);

	print(a_order.price);
