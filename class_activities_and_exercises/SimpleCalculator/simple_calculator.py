#define a class for advanced calculations
class AdvancedCalculator:
    @staticmethod
    def exponentiate(base,exponent):
        return base**exponent

#define functions for basic math operations
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        raise ValueError("cannot divide by zero.")
    return x/y
