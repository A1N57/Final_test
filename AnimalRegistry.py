class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            print(animal)

    def find_animal(self, name):
        for animal in self.animals:
            if animal.get_name() == name:
                return animal
        return None

    def train_animal(self, name, command):
        animal = self.find_animal(name)
        if animal:
            animal.add_command(command)
            print(f"Животное {name} обучено команде: {command}")

    def show_commands(self, name):
        animal = self.find_animal(name)
        if animal:
            print(f"Команды для {name}: {', '.join(animal.get_commands())}")

registry = AnimalRegistry()

#
# dog = Pet("Fido", "2020-01-01")
# dog.add_command("Sit")
# dog.add_command("Stay")
# registry.add_animal(dog)
#
# cat = Pet("Whiskers", "2019-05-15")
# registry.add_animal(cat)
#
# registry.list_animals()
# registry.train_animal("Whiskers", "Jump")
# registry.show_commands("Whiskers")
