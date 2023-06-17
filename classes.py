
# Class: blueprint for creating new objects
# objects: instance of a class

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"polint(self{self.x}, {self.y})")


point = Point.zero()
point.draw()
