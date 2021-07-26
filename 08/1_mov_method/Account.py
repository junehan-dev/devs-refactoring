class Account:
	def __init__(self, od_days, t):
		self.days_overdrawn = od_days;
		self.type = t;

	@property
	def overdraft_charge(self):
		if (self.type["premium"]):
			basecharge = 10;
			if (self.days_overdrawn <= 7):
				return (basecharge);
			else:
				return (basecharge + (self.days_overdrawn - 7) * 0.85);
		return (self.days_overdrawn * 1.75);

	@property
	def base_charge(self):
		result = 4.5;
		result += self.overdraft_charge if (self.days_overdrawn > 0) else 0;
		return (result);

if __name__ == "__main__":
	ac = Account(20, {"premium": 0});
	print(ac.base_charge);
