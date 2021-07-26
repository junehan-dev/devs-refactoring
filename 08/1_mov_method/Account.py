from AccountType import AccountType

class Account:
	def __init__(self, od_days, t:AccountType):
		self.days_overdrawn = od_days;
		self.type = t;

	@property
	def bank_charge(self):
		result = 4.5;
		result += self.type.charge(self.days_overdrawn) if (self.days_overdrawn > 0) else 0;
		return (result);

if __name__ == "__main__":
	ac = Account(20, AccountType(True));
	print(ac.bank_charge);
