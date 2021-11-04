from dataclasses import dataclass

@dataclass
class Amount:
	label:	str;
	price:	int;
	v:		int;
	
	def multiply(self, v):
		return (self.price * (v + 0.1) if ("customer" in self.label) else self.price * v);

	def subtract(self, v):
		self.price -= v;

	def __str__(self):
		return f"{self.label}: {self.price}won, for {self.v}";
