class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)


point = Point(11, 26)
other = Point(10, 12)
combined(point + other)
print(combined.x)
