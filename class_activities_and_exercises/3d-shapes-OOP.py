"""
Teagan Stewart
w0302952
OOP 3d shapes
Febuary 1st, 2024
https://github.com/teagz17/PROG1400
"""
#step 1: define the class
class Cube:
    def __init__(self,length):
        self.length = length
    def calcVol(self):
        return self.length**3
    def calcSurfArea(self):
        return 4 * (self.length**2)
    def calcPerim(self):
        return 12 * self.length
#step 2: create the object
my_cube = Cube(length=5)
#step 3: access object attributes
print(f'cube side length: {my_cube.length}')
#step 4: call object methods
cubeVol = my_cube.calcVol()
cubeSurfArea = my_cube.calcSurfArea()
cubePerim = my_cube.calcPerim()
print('cube volume:',cubeVol)
print('cube surface area:',cubeSurfArea)
print('cube perimiter:',cubePerim)

class Cuboid(Cube):
    def __init__(self,length,width,height):
        super().__init__(length)
        self.width = width
        self.height = height
    def calcVol(self):
        return self.length * self.width * self.height
    def calcSurfArea(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
    def calcPerim(self):
        return 4 * (self.length + self.width + self.height)

my_cuboid = Cuboid(length=8,width=4,height=3)

print(f'cuboid length: {my_cuboid.length}\ncuboid width: {my_cuboid.width}\ncuboid height: {my_cuboid.height}')

cuboidVol = my_cuboid.calcVol()
cuboidSurfArea = my_cuboid.calcSurfArea()
cuboidPerim = my_cuboid.calcPerim()
print(f'cuboid volume: {cuboidVol}\ncuboid surface area: {cuboidSurfArea}\ncuboid perimiter: {cuboidPerim}')