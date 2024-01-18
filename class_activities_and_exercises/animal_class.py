#demonstrate inheritance
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    
class Dog(Animal):
    def speak(self):
        return f'{self.name} says woof!'
    
class Cat(Animal):
    def speak(self):
        return f'{self.name} says meow!'
    
#create object
dog = Dog('Jenny', 'house')
cat = Cat('Archie', 'house')

#use methods
print(f'{dog.name}')
print(f'{dog.speak()}')
print(f'{cat.speak()}')