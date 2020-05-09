n=int(input("enter number"))
rev=0
while n>0: 
	rem=int(n%10)
	rev=int(rev*10+rem)
	n=int(n/10)
print("reverse is",rev)