class Employee:
	name=input("enter name")
	ID=int(input("enter your eid"))
	def Increment(self,bsal):
		self.bsal=bsal
		self.hra= (25/100)*self.bsal
		self.gross=self.bsal+self.hra
		print("gross",self.gross)
obj1=Employee()
obj1.Increment(1000)
print("name:",getattr(obj1,"name"))
print("eid:",getattr(obj1,"ID"))
print("gross salary",getattr(obj1.Increment,""))
#obj2=Employee()
#Increment()
#eid,obj=total sal, (basic sal,hra,da)

		