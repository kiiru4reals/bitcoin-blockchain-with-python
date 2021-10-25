from finite_fields import FieldElement

a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)

print(b == a)
print(a + b == c)
print(a + b == c)
print(a * b == c)

a = FieldElement(7, 13)
b = FieldElement(8, 13)
print(a ** -3 == b)

