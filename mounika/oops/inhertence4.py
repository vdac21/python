#Hierarical inheritence

class parent():
    def output(self):
        print(" i  am parent")
class child1(parent):
    def outputc(self):
        print("child1")
class child2(parent):
    def outputd(self):
        print("child2")
c=child1()
c1=child2()
c1.output()

c1.outputd()

c.output()
c.outputc()

