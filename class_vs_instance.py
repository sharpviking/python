
class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"polint(self{self.x}, {self.y})")


point = Point(11, 26)
point(point.default_color)
point.z = 10
point.draw()


another = Point(3, 4)
another.draw()
