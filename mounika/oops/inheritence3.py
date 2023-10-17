#multiple inheritence


class father():
    def output(self):
        print("i am father")
class mother():
    def out(self):
        print("i am mother")
class child(father,mother):
    def outputc(self):
        print("i am child")

c=child()
c.output()
c.out()
c.outputc()
