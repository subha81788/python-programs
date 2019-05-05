class Person:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True

emp = Employee("Geek1")
print("{0} is an employee: {1}".format(emp.getName(),emp.isEmployee())) 
shop_keeper = Person("Geek2")
print("{0} is an employee: {1}".format(shop_keeper.getName(),shop_keeper.isEmployee()))
