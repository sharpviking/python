class Point:

    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point.default_color = "yellow"
point = Point(1, 2)
print(point.default_color)
point.z = 10

print.draw()

another = Point(3, 4)
another.draw()
