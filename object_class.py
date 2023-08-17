class Animal:


class Mammal(Animal):


m = Mammal()
print(isinstance(m,object))
o=object()
issubclass(Mammal,Animal)
