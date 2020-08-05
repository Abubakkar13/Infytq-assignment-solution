#OOPR-Assgn-8
#Start writing your code here
class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
    
    def set_student_id(self, student_id):
        self.__student_id = student_id
    def set_marks(self, marks):
        self.__marks = marks
    def set_age(self, age):
        self.__age = age
    
    def get_student_id(self): return self.__student_id
    def get_marks(self): return self.__marks
    def get_age(self): return self.__age
    
    def validate_marks(self):
        return self.get_marks() in range(0, 101)
    
    def validate_age(self):
        return self.get_age() > 20
    
    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            return self.get_marks() >= 65
        return False

student = Student()
student.set_student_id(1000)
student.set_marks(44)
student.set_age(21)
print(student.check_qualification())
