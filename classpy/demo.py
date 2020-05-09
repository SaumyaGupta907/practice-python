class Circle:
	pi=3.14
	def __init__(self,r):
		self.r=r
	def area(self):
		area=Circle.pi*self.r*self.r
		return area
	def perimeter(self):
		return 2*Circle.pi*self.r
class Demo:
	def accesscircle(self):
		ob1=Circle(5)
		print("Area of circle is",ob1.area())
		print("Perimeter of circle is",ob1.perimeter())
ob=Demo()
ob.accesscircle()