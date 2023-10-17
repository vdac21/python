class Pen1:
    def get_color(self):
        print("blue in color")

class Pen2:
    def get_color(self):
        print("red in color")

obj_p1=Pen1()
obj_p2=Pen2()
def color(obj):
    obj.get_color()

color(obj_p1)
color(obj_p2)


num=input("enter a number: ")
sum=0
for i in num:
    sum+=int(i)**3
if sum == int(num):
    print("armstrong")
else:
    print("not  a armstrong")
