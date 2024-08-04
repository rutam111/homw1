class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        self.salary = 0

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.salary = new_salary
        else:
            print("Salary cannot be negative!")

    def get_annual_salary(self):
        return self.salary * 12

class Director(Employee):
    pass  # Additional methods specific to Director can be added here

class Accountant(Employee):
    pass

director = Director("Alice", 101)
director.set_salary(8000)
print(f"{director.name}'s annual salary: ${director.get_annual_salary()}")

accountant = Accountant("Bob", 102)
accountant.set_salary(6000)
print(f"{accountant.name}'s monthly salary: ${accountant.get_salary()}")
