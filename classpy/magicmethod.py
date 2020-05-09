class Time: 
	def __init__(self,h,m):
		self.h=h
		self.m=m
	def __add__(self,t):
		temp=Time(0,0)
		temp.m=self.m+ t.m
		if(temp.m>=60):
			temp.h=self.h+t.h+1
			temp.m=temp.m%60
		else:
			temp.h=self.h+t.h
		return temp
	def display(self):
		print(self.h,":",self.m)
t1=Time(3,40)
t2=Time(4,30)
res=t1+t2
print("Time1:",end=" ")
t1.display()
print("Time2:",end=" ")
t2.display()
print("sum of above timings are:",end=" ")
res.display()
