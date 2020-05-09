"""In any object-oriented programming language, overriding is a feature that allows a sublass or child class to provide a specific implementation of a method that is already provided by its super-class or parent class"""
#Another way of creating abstract methods and classes

from abc import ABC,abstractmethod
class Polygon(ABC):
	#abstract method
	@abstractmethod         #optional
	def noofsides(self):
		pass
class Triangle(Polygon):
	#overriding abstract method
	def noofsides(self):
		print("I have 3 sides")
class Pentagon(Polygon):
	#overriding abstract method
	def noofsides(self):
		print("I have 5 sides")
class Hexagon(Polygon):
	#overriding abstract method
	def noofsides(self):
		print("I have 6 sides")
class Quadrilateral(Polygon):
	#overriding abstract method
	def noofsides(self):
		print("I have 4 sides")
# Driver code
R=Triangle()
R.noofsides()

K=Quadrilateral()
K.noofsides()

R=Pentagon()
R.noofsides()

K=Hexagon()
K.noofsides()

"""following conditions must be met for overriding a function:
1)Inheritance should be there.Function overriding cannot be done within a class.We need to derive a child class from a parent clSS.
2)The function that is redefined in the child class should have the same signature as in the parent class i.e,same number of parameters"""  