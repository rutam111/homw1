class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def sound(self):
        pass

    def move(self):
        pass

    def sleep(self):
        pass

class Carnivore(Animal):
    def __init__(self, name, habitat, fang_size):
        super().__init__(name, habitat)
        self.fang_size = fang_size

    def hunt(self):
        print(f"{self.name} is hunting with {self.fang_size} cm long fangs.")

    def roar(self):
        print(f"{self.name} roars loudly.")

    def camouflage(self):
        print(f"{self.name} uses its surroundings to blend in.")

class Herbivore(Animal):
    def __init__(self, name, habitat, horn_length):
        super().__init__(name, habitat)
        self.horn_length = horn_length

    def graze(self):
        print(f"{self.name} is grazing with its {self.horn_length} cm long horns.")

    def run(self):
        print(f"{self.name} runs quickly to escape predators.")

    def socialize(self):
        print(f"{self.name} lives in a group and communicates with others.")

# Создание объектов классов
lion = Carnivore(name="Lion", habitat="Savannah", fang_size=8)
deer = Herbivore(name="Deer", habitat="Forest", horn_length=30)

# Вызов методов
lion.hunt()
lion.roar()
lion.camouflage()

deer.graze()
deer.run()
deer.socialize()
