#multilevel inheritance (classwork)
class Area:
	def __init__(self,r):
		self.r=r
	def areas(self):
		return 3.14*self.r*self.r
class Perimeter(Area):
	def __init__(self,r):
		Area.__init__(self,r)
		self.r=r
		print("this class inherits features from Area")
	def perimeters(self):
		return 2*3.14*self.r
class Circle(Perimeter):
	def __init__(self,r):
		Perimeter.__init__(self,r)
		print("This class inherits features from Perimeter")
	def display(self):
		print("Area of circle is",Area.areas(self))
		print("perimeter of circle is",Perimeter.perimeters(self))
x1=int(input("enter an integer:"))
c1=Circle(x1)
c1.display()
x2=int(input("enter inetger:"))
a1=Area(x2)
print("area of class is",a1.areas())
x3=int(input("enter an integer"))
p1=Perimeter(x3)
print("perimeter of circle is",p1.perimeters())