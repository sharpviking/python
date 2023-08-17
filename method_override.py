class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        print('Mammal Constructor')
        self.weight = 26
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()

print(m.age)
