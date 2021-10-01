class FieldElement:
    def __init__(self,num, prime):
        if num >= prime or num<0:
            error = "{} is not in range of 0  and {}".format(num, prime)
            raise ValueError(error)
        self.num = num
        self.prime = prime
    def __repr__(self):
        return "FieldElement_{}({})".format(self.num, self.prime)
    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime