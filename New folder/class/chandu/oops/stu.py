class Student:
    s_id=101
    def __init__(self,s_name):
        self.s_name=s_name
    def get_student_name(self):
        print(self.s_name)


        
obj_student=Student("avi")
obj_student1=Student("anu")

obj_student.get_student_name()

"""print(Student.s_id)
print(obj_student.s_id)
print(obj_student1.s_id)"""

obj_student.s_id=104
print(Student.s_id)
print(obj_student.s_id)
print(obj_student1.s_id)
"""
Student.s_id=103
print(Student.s_id)
print(obj_student.s_id)
print(obj_student1.s_id)

"""
