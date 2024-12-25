
class Operation:
    def calculate(self, a, b):
        pass


class Addition(Operation):
    def calculate(self, a, b):
        return a + b


class Subtraction(Operation):
    def calculate(self, a, b):
        return a - b


class Multiplication(Operation):
    def calculate(self, a, b):
        return a * b


a=10
b=5
operations=[Subtraction(),Multiplication(),Addition()]
for operation in operations:
    print(operation.calculate(a,b))