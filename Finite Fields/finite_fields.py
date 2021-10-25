"""
Constructing a Finite Field in Python
"""

class FieldElement:
    """
    A class that represents a single field element.
    Represents an element in the field prime
    """

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = f"Num {num} not in the field range 0 to {prime - 1}"
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return f"FieldElement_{self.prime}({self.num})"

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    # Exercise 1
    def __ne__(self, other):
        return not(self == other)

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError(f'{self.num} and {self.prime} are not in the same field.')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    # Exercise 3
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError(f'{self.num} and {self.prime} are not in the same field.')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    # Exercise 6
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError(f'{self.num} and {self.prime} are not in the same field.')
        num = (self.num * other.num) % other.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        x = exponent % (self.prime - 1)
        num = pow(self.num, x, self.prime)
        return self.__class__(num, self.prime)

    # Exercise 9
    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError(f'{self.num} and {self.prime} are not in the same field.')
        num = self.num * pow(other.num, self.prime - 2, self.prime) % self.prime
        return self.__class__(num, self.prime)



