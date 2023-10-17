#create a class with instance attributes

class vechicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
model=vechicle(240,18)
print(model.max_speed,model.mileage)



class parent():
    def fun(self):
        print("hello!..")
class child():
    def fun1(self):
        print("hi!..")
class child2(parent,child):
     def fun2(self):
        print("hi,hello..")
obj=child2()

obj.fun()
obj.fun1()
obj.fun2()


class emp():
    def sal(self):
        print("heelo")
class sal():
    def fun1(self):
        print("hi")
class des():
    def fun2():
        print("nmm")
