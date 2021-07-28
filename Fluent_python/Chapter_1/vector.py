from math import pow, sqrt


class Vector:
    """Vector representation"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add vector object to other vector object"""
        if isinstance(other, Verctor):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)
        raise ValueError("Only vector addition is supported")

    def __mul__(self, other):
        """Multiply vector by scalar"""
        if isinstance(other, int) or isinstance(other, float):
            x = self.x * other
            y = self.y * other
            return Vector(x, y)

    def __bool__(self):
        """Find sign"""
        return bool(abs(self))

    def __abs__(self):
        """Length of vector"""
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __repr__(self):
        """String representation of vector"""
        return f"Vector({self.x}, {self.y})"


if __name__ == '__main__':
    v1 = Vector(3, 4)
    v2 = Vector(5, 5)

    print("Vector 1: ", v1)
    print("Vector 2: ", v2)

    print("Absolute value of v1: ", abs(v1))
    print("Absolute value of v2: ", abs(v2))

    print("Multiply v1 by 2: ", v1 * 2)
