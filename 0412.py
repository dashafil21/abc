class Vector:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector( self.x + other.x, self.y + other.y)


print(Vector(1,3) + Vector(2,4))

class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


    def __add__(self, other):
        new_denominator=self.denominator*other.denominator
        new_numerator=self.numerator*other.denominator + self.denominator*other.numerator
        return Fraction(new_numerator,new_denominator)


a=Fraction(1,3)
b=Fraction(2,6)
print(a+b)


