class Point:
    def __ne__(self, other):
        return not (self == other)