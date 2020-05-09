#multiple inheritance
class Area:
	def __init__(self,r):
		self.r=r
	def areas(self):
		return 3.14*self.r*self.r
class Perimeter:
	def __init__(self,r):
		self.r=r
	def perimeters(self):
		return 2*3.14*self.r
class Circle(Area,Perimeter):
	def __init__(self,r):
		Area.__init__(self,r)
		print("This class inherits features from two classes")
	def display(self):
		print("Area of circle is",Area.areas(self))
		print("perimeter of circle is",Perimeter.perimeters(self))
x=int(input("enter an integer:"))
c1=Circle(x)
c1.display()