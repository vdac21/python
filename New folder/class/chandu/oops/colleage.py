class college:
    name=None
    def __init__(self,college_name,courses):
        self.college_name=college_name
        self.courses=courses
    def get_college_name(self):
        print(self.college_name)
    def get_courses(self):
        print(self.courses)
    def add_courses(self,courses):
        self.courses=courses
        print("modified courses",courses)
 
obj1= college("gfgc",['bca','bsc'])
obj1.get_college_name()
obj1.get_courses()
obj1.add_courses(['bcom','ba'])
print(obj1.courses)
obj2 = college("reva",['bba','homescience'])
obj2.get_college_name()
obj2.get_courses()
obj2.add_courses(['msc','mba'])
print(obj2.college_name)
'''obj2.college_name="women's college"
print(obj1.college_name)
print(obj2.college_name)
college.name="govt pu college"
print(obj1.name)
print(obj2.name)'''
