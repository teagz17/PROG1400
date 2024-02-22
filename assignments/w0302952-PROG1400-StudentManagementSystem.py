"""
w0302952
Teagan Stewart
PROG1400
February 22nd, 2024
Student Manageent System assignment
"""

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        return f'Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}'

    def update_grade(self):
        pass

class GraduateStudent(Student):
    def __init__(self, student_id, name, age, grade, thesis_topic):
        super().__init__(student_id, name, age, grade)
        self.thesis_topic = thesis_topic
    
    def display_info(self):
        pass

class StudentManagementSystem():
    def __init__(self):
        self.students = []
    
    def display_all_students():
        pass

    def search_student_by_id(self, student_id):
        print('Search student:')
        for s in self.students:
            if s.student_id == student_id:
                print('Student found')
                s.display_info()
                return
            print('Student not found')
        

    def update_grade_by_id():
        pass