class vdac:
    def __init__(self,name):
        self.name=name
    def course_details(self,name):
        self.name=name
        print("course name is",self.name)
obj_vdac=vdac('python')
obj_vdac.course_details('c')
