"""
abstraction:
"""
class A:
    def method(self):
        pass
obj1=A()
obj1.method()
"""abc module"""



from abc import ABC,abstactmethod
class A(ABC):
    @abstractmethod
    def method(self):
        pass
obj1=A()
obj1.method()



# Python program showing
# abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

	@abstractmethod
	def noofsides(self):
		pass

class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 3 sides")

class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 5 sides")

class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have 4 sides")

# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()
