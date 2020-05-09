#example for abstract class and abstract methods
class Polygon:
	def getData(self):
		raise NotImplementedError
	def area(self):
		raise NotImplementedError
class Rectangle(Polygon):
	def getData(self):
		self.l=int(input("enter length of rectangle"))
		self.b=int(input("enter width of rectangle"))
	def area(self):
		return self.l*self.b
class Triangle(Polygon):
		def getData(self):
			self.b=int(input("Enter breadth of the triangle"))
			self.h=int(input("enter height of the triangle"))
		def area(self):
			return 0.5*self.b*self.h
r=Rectangle()
r.getData()
print("Area of rectangle",r.area())

t=Triangle()
t.getData()
print("Area of triangle",t.area())
