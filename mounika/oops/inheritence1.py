#single inheritence
class parent():
    def out(self):
        print("i am the parent")
class child(parent):
    def output(self):
        print(" i am the child")
c=child()
c.output()
c.out()
