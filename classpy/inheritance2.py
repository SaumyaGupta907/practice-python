class A:
	def __init__(self,a):
		self.a=a
	def a(self):
		print("class A variable")
		print(self.a)
	def display(self):
		A.a(self)
obj=A(10)
obj.display()
