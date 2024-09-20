class Animal:
    def __init__(self, name, birth_date):
        self.__name = name
        self.__birth_date = birth_date
        self.__commands = []

    def add_command(self, command):
        self.__commands.append(command)

    def get_commands(self):
        return self.__commands

    def __str__(self):
        return f"{self.__name}, родился: {self.__birth_date}"

class Pet(Animal):
    pass

class PackAnimal(Animal):
    pass
