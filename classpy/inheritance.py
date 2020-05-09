class Person:
	def __init__(self,fname,lname):
		self.firstname=fname
		self.lastname=lname
	def printname(self):
		print(self.firstname,self.lastname)
class Student(Person):
	def __init__(self,fname,lname):                #optional
		Person.__init__(self,fname,lname)      #optional
	def sinfo(self,rno,branch):
		self.rollno=rno
		self.branch=branch
		print(self.rollno)
		print(self.branch)
class Employee(Person):
	def __init__(self,fname,lname):
		Person.__init__(self,fname,lname)
	def einfo(self,eid,dept):
		self.eid=eid
		self.dept=dept
		print(self.eid)
		print(self.dept)
p=Person("Saumya","Gupta")
p.printname()
e=Employee("Sid","ghosh")
e.printname()
e.einfo("4016","CSE")
s=Student("hrithika","panguluri")
s.printname()
s.sinfo("18911A05D9","CSE")