#polymorphism
class Fruit:
    #constructor (__init__)
    def __init__(self, name):
        self.name = name
    #method to return str 'Generic Taste'
    def taste(self):
        return 'Generic Taste'

class Apple(Fruit):
    def __init__(self, name, colour):
        #calling the superclass method
        super().__init__(name)
        self.colour = colour
    
    def taste(self):
        generic_taste = super().taste()
        return f'{generic_taste} and crisp'

class Orange(Fruit):
    def __init__(self, name, colour):
        #calling the superclass method
        super().__init__(name)
        self.colour = colour
    
    def taste(self):
        generic_taste = super().taste()
        return f'{generic_taste} and sweet'

def describe_taste(fruit):
    print(f'{fruit.name} tastes: {fruit.taste()}')

#create instances of apple and orange
apple = Apple('Red Apple', 'Red')
orange = Orange('Orange Orange', 'Large')

#demonstrate polymorphism by calling the describe_taste function with different fruit objects
describe_taste(apple)
describe_taste(orange)