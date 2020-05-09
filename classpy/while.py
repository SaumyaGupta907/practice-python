#reverse of a number
n=int(input("enter a number"))
rev=0
while n>0:
	rem=n%10
	rev=rev*10+rem
	n=int(n/10)
print("the reverse is",rev)