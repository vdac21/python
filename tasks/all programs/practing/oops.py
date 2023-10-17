class rect:
    def __init__(self, x, y):
        self.w = x
        self.h = y


    def move(self):
        self.x = self.x + 100
        self.y = self.y + 100

    def display(self):
        print(f"width : {} height: {}" .format(self.w, self.h))

r1 = rect(10, 20)
r2 = rect(100,200)


r1.display()
r2.display()
r2.move()
r1.display()
r2.display()



        
