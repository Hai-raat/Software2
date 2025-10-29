# 1. Create base class: Animal
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        print("Some animal sound")

    def info(self):
        print(f"\nName: {self.name}. \nSpecies: {self.species}.")


# 2. Create subclasses: Lion, Elephant, Snake
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion")

    def sound(self):
        print("Roooaaaaar!")


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant")

    def sound(self):
        print("Puuuuuuhhh!")


class Snake(Animal):
    def __init__(self, name):
        super().__init__(name, "Snake")

    def sound(self):
        print("Hissss!")


# 3. Create class: Zoo
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_info(self):
        print(f"There are {len(self.animals)} animals in the zoo:")
        for animal in self.animals:
            animal.info()

    def make_sounds(self):
        print("\nAnimal sounds in the zoo:")
        for animal in self.animals:
            animal.sound()


# main program
zoo = Zoo()

lion = Lion("Scar")
elephant = Elephant("Ella")
snake = Snake("Pumba")

zoo.add_animal(lion)
zoo.add_animal(elephant)
zoo.add_animal(snake)

zoo.display_info()
zoo.make_sounds()
