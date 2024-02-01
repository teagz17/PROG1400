class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
    def calculate_volume(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimiter(self):
        return 4 * (self.length + self.width + self.height)
    def calculate_volume(self):
        return self.width * self.length * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(length=side_length, width=side_length, height=side_length)

class Circle(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def calculate_area(self):
        return 3.14 * self.radius**2
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    def calculate_volume(self):
        return self.height * (3.14 * self.radius**2)

def print_area(shape):
    print(f'area of the {shape} is {shape.calculate_area()}')

def print_circumference(shape):
    print(f'circumference of the {shape} is {shape.calculate_perimeter()}')

def print_volume(shape):
    print(f'volume of the {shape} is {shape.calculate_volume()}')

rect3d = Rectangle(length=5, width=5, height=5)
square3d = Square(side_length=5)
circle3d = Circle(radius=5, height=5)

print_area(rect3d)
print_circumference(rect3d)
print_volume(rect3d)
