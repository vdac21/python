#input list

x=[450,540,1256,2506,15342,32424,20018,56300]
y=[]#place holder to store all the numbers which are divisible by 4

total=0 #place holder to add all the numbers from y

for e in x:
    if e%4==0:
        y.append(e)
        total=total+e
print(f"given input:{x}")
print(f"Elements which are divisible by 4:{y}")
print(f"Sum of elements which are divisible by 4:{total}")
class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


# inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')


# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()
 
