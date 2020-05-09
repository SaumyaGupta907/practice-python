#factorial
n=int(input("enter a number"))
fact=1
for i in range(2,n+1):
	fact=fact*i
	i+=1
print("factorial is",fact)