#Multilevel inheritence

class gf():
    def outputgf(self):
        print("i am gf")
class parent(gf):
    def output(self):
        print("i am parent")
class child(parent):
    def out(self):
        print("i am child")
c=child()
c.outputgf()
c.output()
c.out()
