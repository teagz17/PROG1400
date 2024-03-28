'''
w0302952
Teagan Stewart
PROG1400
February 29th, 2024
Exploring Object-Oriented Programming in Python
'''
#task 1: abstraction
class Shape: #main class
    def __init__(self, length, width, radius): #initializes and defines the attributes
        self.length = length
        self.width = width
        self.radius = radius
    
    def area(self): #method to calculate area
        return self.length * self.width

class Rectangle(Shape): #subclass for rectangles
    def __init__(self, length, width, radius):
        super().__init__(length, width, radius) #inherits attributes from parent class
    
    def area(self): #inherents the area method from parent class
        return super().area()
    
class Circle(Shape): #subclass for circles
    def __init__(self, length, width, radius):
        super().__init__(length, width, radius)
    
    def area(self): #the formula for finding the area of a circle is different, so it doesn't inherit the area method from the parent class
        return 3.14 * self.radius ** 2

rectangle1 = Rectangle(5, 3, 0) #defining the rectangle and its attributes in the order they appear in the __init__ method; rectangles dont have a radius, so we use 0 in its place
circle1 = Circle(0, 0, 3) #ditto^^

print(f"area of rectangle: {rectangle1.area()}") #prints the results of the function
print(f"area of circle: {circle1.area()}")

#task 2: encapsulation
class Student: #main class
    def __init__(self):
        self.__name = '' #left blank because the user inputs the name
        self.__age = 0 #same as above, but since the age is an integer it's 0 instead of being left blank
        self.__grade = '' #same as name

    def set_info(self, name, age, grade):
        self.__name = name #sets the attributes to be equal to the input
        self.__age = age
        self.__grade = grade

    def get_info(self): #method to return the student's details
        return f'Student name: {self.__name} \nage: {self.__age} \ngrade: {self.__grade}'
    
student1 = Student() #student variable
name = input('enter student name: ') # prompts the user to enter the student info
age = input('enter student age: ')
grade = input('enter student grade: ')

student1.set_info(name, age, grade) #calls the method
print(student1.get_info()) #prints the result

#task 3: inheritance
class Animal: #main class
    def __init__(self, name): 
        self.name = name
    
    def speak(self):
        pass
    
    def move(self):
        pass
    
class Dog(Animal): #subclass for dogs
    def __init__(self, name): #inherits 'self' variables from parent class
        super().__init__(name)
    
    def speak(self): #defines "speak" method for the dog
        return f'{self.name} says woof!'
    
    def move(self): #defines 'move' method for the dog
        return f'{self.name} is walking.'

class Cat(Animal): #subclass for cats
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return f'{self.name} says meow!'
    
    def move(self):
        return f'{self.name} is sleeping.'
    
class Bird(Animal): #subclass for birds
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        return f'{self.name} says chirp chirp!'
    
    def move(self):
        return f'{self.name} is flying.'

dog1 = Dog('Dogmeat') #defines the dog and its name
cat1 = Cat('Korin') 
bird1 = Bird('Kass')

print(dog1.speak(), dog1.move()) #prints the dog's actions by using the methods
print(cat1.speak(), cat1.move())
print(bird1.speak(), bird1.move())

#task 4: polymorphism
class Vehicle: #main class
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def travel(self):
        pass

class Car(Vehicle): #car subclass
    def __init__(self, make, model): #inherits the attributes from the parent class
        super().__init__(make, model)
    
    def travel(self): #defines the travel method for cars
        print(f'the {self.make} {self.model} is driving.')
    
class Plane(Vehicle): #plane subclass
    def __init__(self, make, model):
        super().__init__(make, model)

    def travel(self):
        print(f'the {self.make} {self.model} is flying.')
    
class Bicycle(Vehicle): #bike subclass
    def __init__(self, make, model):
        super().__init__(make, model)
    
    def travel(self):
        print(f'the {self.make} {self.model} is cycling.')

car1 = Car('hyundai', 'elantra') #defines the object and its attributes
plane1 = Plane('boeing', '747')
bike1 = Bicycle('mongoose', 'legion')

for x in (car1, plane1, bike1): #calls the method to print the vehicle's action using a "for loop"; it loops through the vehicles and calls the method for each one 
    x.travel()