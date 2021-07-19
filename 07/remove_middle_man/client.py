from person import Person, Department, Manager

if __name__ == "__main__":
	aPerson = Person("", Department("A32", Manager("manageman")));
	manager = aPerson.department.manager;
	print(manager.name);
