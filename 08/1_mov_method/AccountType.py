class AccountType:
	def __init__(self, p):
		self.ispremium = p;

	def charge(self, overdrawn_days):
		if (self.ispremium):
			basecharge = 10;
			if (overdrawn_days <= 7):
				return (basecharge);
			else:
				return (basecharge + (overdrawn_days - 7) * 0.85);
		return (overdrawn_days * 1.75);

