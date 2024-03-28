class Student:
    def __init__(self):
        self.__name = ''
        self.__age = 0
        self.__grade = ''

    def set_info(self, name, age, grade):
        self.__name = name
        self.__age = age
        self.__grade = grade

    def get_info(self):
        return f'Student name: {self.__name}, age: {self.__age}, grade: {self.__grade}'
    
student1 = Student()
name = input('enter student name: ')
age = input('enter student age: ')
grade = input('enter student grade: ')

student1.set_info(name, age, grade)
print(student1.get_info())