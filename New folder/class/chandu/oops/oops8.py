class Engine:
    year=2000

class car:
    def __init__(self,carmodel):
       self.carmodel=carmodel
       print(self.carmodel)
       obj_Engine=Engine()
obj_car=car("swift")
