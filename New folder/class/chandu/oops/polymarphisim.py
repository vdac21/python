class pen1:
    def get_color(self):
        print("blue in color")

class pen2:
    def get_color(self):
        print("red in color")

obj_p1=pen1()
obj_p2=pen2()

def color(obj):
    obj.get_color()

color(obj_p1)
color(obj_p2)

    

    
