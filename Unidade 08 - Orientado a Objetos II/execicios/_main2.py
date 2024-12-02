class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError("Operand must be an instance of Point")
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
# Teste:
a = Point(3, 4)
b = Point(1, 2)
print(a + b)  # Point(4, 6)