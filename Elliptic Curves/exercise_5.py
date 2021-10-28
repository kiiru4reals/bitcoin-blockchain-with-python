def __add__(self, other):
    if self.a != other.a or self.b != other.b:
        raise TypeError
    if self.x is None:
        return other
    if other.x is None:
        return self

    if self.x != other.x:
        s = (other.y - self.y) / (other.x - self.x)
        x = s**2 - self.x - other.x
        y = s * (self.x - x) - self.y
        return self.__class__(x, y, self.a, self.b)
