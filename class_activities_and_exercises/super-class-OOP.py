#step 1: define the class
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimiter(self):
        return 2 * (self.length + self.width)

#step 2: create the object
my_rectangle = Rectangle(length=5, width=3)

#step 3: access object attributes
print(f'rectangle length: {my_rectangle.length}')
print(f'rectangle width: {my_rectangle.width}')

#step 4: call object methods
area = my_rectangle.calculate_area()
perimiter = my_rectangle.calculate_perimiter()
print('rectangle area:',area)
print('rectangle perimiter:',perimiter)

#3d rectangle
class Rectangle_3D:
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height
    def calculate_volume(self):
        return self.length * self.width * self.height
    def calculate_surfArea(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
    def calculate_3dperimiter(self):
        return 4 * (self.length + self.width + self.height)

my_rectangle3d = Rectangle_3D(length=5, width=3, height=2)

print(f'cuboid length: {my_rectangle3d.length}')
print(f'cuboid width: {my_rectangle3d.width}')
print(f'cuboid height: {my_rectangle3d.height}')

volume = my_rectangle3d.calculate_volume()
surfArea = my_rectangle3d.calculate_surfArea()
perimiter3d = my_rectangle3d.calculate_3dperimiter()
print('cuboid volume:',volume)
print('cuboid surface area:',surfArea)
print('cuboid perimeter:',perimiter3d)

#inheritance
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(length=side_length, width=side_length)

my_square = Square(side_length=5)

print(f'square length: {my_square.length}')
print(f'square width: {my_square.width}')

area_square = my_square.calculate_area()
perimeter_square = my_square.calculate_perimiter()
print('square area:',area_square)
print('square perimiter:',perimeter_square)