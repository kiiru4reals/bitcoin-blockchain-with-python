class FieldElement:
    # Initialisation
    def __init__(self,num,prime):
        if num >=prime or num <0:
            error = "{} is in range of {}".format(num,prime)
            raise ValueError(error)
        # Declare attributes here
        self.num = num
        self.prime = prime
    # Creating the set now
    def __req__(self):
        return("FieldElement_{}({}).{}".format(self.num,self.prime))
    # Defining modulo here
    def __modz__(self,other):
        determinant = self.other + self.num % self.prime
        if determinant:
            return "Finite set is closed and answer is {}".format(determinant)
        else: 
            return "Yikes!"