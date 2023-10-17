class vechicle:

    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def show(self):
        print('Details:',self.name, self.color,self.price)
    def max_speed(self):
        print("vechicle maximum speed is 150")
    def change_gear(self):
        print("vechicle change 6 gear")
#inherit from vechicle class
class car(vechicle):
    def max_speed(self):
        print("vechicle maximum speed is 240")
    def change_gear(self):
        print("vechicle change 7 gear")
#car object
car=car("car x1","Red",20000)
car.show()

car.max_speed()
car.change_gear()
#vechicle object
vechicle=vechicle('truck x1','white',76000)
vechicle.show()
vechicle.max_speed()
vechicle.change_gear()
              

        
