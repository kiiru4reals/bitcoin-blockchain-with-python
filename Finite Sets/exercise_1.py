class FieldElement:
    def __init__(self,num,prime):
        if num>=prime or num<0:
            error = "{} is not in the range of 0 and {}".format(num,prime)
            ValueError= error
        self.num=num
        self.prime=prime
    def __ne__(self,other):
        return not (self == other)