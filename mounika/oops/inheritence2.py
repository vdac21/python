#Multilevel inheritence
class gf():
    def outputgf(self):
        print("i am gf")

class parent(gf):
    def output(self):
        print("i am the father")

class child(parent):
    def out(self):
        print("i am the child")


c=child()
c.outputgf()
c.output()
c.out()
    
