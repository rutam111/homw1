class Vehicle:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle: {self.model} ({self.year}), made by {self.company}")

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass 

car1 = Car("Toyota", "Camry", 2022)
car1.display_info()

truck1 = Truck("Ford", "F-150", 2021)
truck1.display_info()
