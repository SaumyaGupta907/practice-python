#overloading +=operator
class Example:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def __str__(self):
		return "({0},{1})".format(self.a,self.b)
	def __iadd__(self,other):
		self.a+=other.a
		self.b+=other.b
		return Example(self.a,self.b)
obj1 = Example(1,2)
obj2 = Example(2,3)
obj2  += obj1
print (obj2)