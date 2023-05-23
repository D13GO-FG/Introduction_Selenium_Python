class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Allow the caller to retrieve the salary
    def getSalary(self):
        return self.salary

    # Allow the caller to set a new salary
    def setSalary(self, salary):
        self.salary = salary


oPerson1 = Person('Diego Flores', 90000)
oPerson2 = Person('Luis Gonzalez', 99000)
# Get the salaries using getter and print
print(oPerson1.getSalary())
print(oPerson2.getSalary())

# Change the salaries using setter
oPerson1.setSalary(100000)
oPerson2.setSalary(111111)

# Get the salaries and print again
print(oPerson1.getSalary())
print(oPerson2.getSalary())