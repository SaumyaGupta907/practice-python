#overloading > operator
class Example:
	def __init__(self,a):
		self.a=a
	def __gt__(self,other):
		return self.a>other.a
obj1= Example(1)
obj2=Example(2)
print(obj2>obj1)
