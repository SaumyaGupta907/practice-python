#multi level
class name:
	def __init__(self,n):
		self.n=intput("name")
	def names(self):
		print(self.n)
class roll(name):
	def __init__(self,r):
		name.__init__(self,n)
		self.r=r
	def rolls(self):
		print(self.r)
class student(roll):
	def __init__(self,s):
		roll.__init__(self,r)
		self.s=s
	def display(self):
		print("The name of student is",name.names(self))
		print("The roll of student is",roll.rolls(self))
x=input("enter name")
y=int(input("enter roll"))
obj1=roll(x)
obj=student(y)
obj.display()