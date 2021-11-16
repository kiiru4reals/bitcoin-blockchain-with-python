def __add__(self, other):
    if self.a != other.a or self.b != other.b:
        raise TypeError
    if self.x is None:
        return other
    if other.x is None:
        return self
    if self.x == other.x and self.y != other.y:
        return self.__class__(None, None, self.a, self.b)
