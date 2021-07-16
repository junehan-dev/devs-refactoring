class Manager:
	def __init__(self, n):
		self.name = n;

class Department:
	def __init__(self, ch_code, m):
		self._charge_code	= ch_code;
		self._manager = m;

	@property
	def charge_code(self):
		return (self._charge_code);

	@property
	def manager(self):
		return (self._manager);

class Person:
	def __init__(self, name, dp:Department):
		self._name = name;
		self._department = dp;

	@property
	def name(self):
		return (self._name);

	@property
	def department(self):
		return (self._department);

if __name__ == "__main__":
	dp = Department("AB01", Manager("manager1"));
	aPerson = Person("june", dp);

	manager = aPerson.department.manager;
	print(manager.name);
