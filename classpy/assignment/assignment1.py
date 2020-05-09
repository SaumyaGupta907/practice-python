while 1:
	l=[]
	print("Enter your choice\n")
	n=int(input("1. Enter marks\n 2.Average marks\n"))
	if n==1:
		name=input("Enter your name:")
		roll=int(input("Enter your roll number:"))
		year=int(input("Enter year"))
		branch=input("Enter your branch")
		print("Choose your semester")
		sem=int(input("1. 2."))
		if sem==1:
			m1=int(input("Enter m1 marks:"))
			chem=int(input("Enter chemistry marks:"))
			phy=int(input("Enter physics marks:"))
			total= m1 + chem + phy
			print("Your semester 1 total is",total)
			l.append(total)
		elif sem==2:
			python=int(input("Enter python marks:"))
			ds=int(input("Enter ds marks:"))
			java=int(input("Enter java marks:"))
			total1= python + ds + java
			print("Your semester 2 total is",total1)
			l.append(total1)
		else:
			print("Enter valid option")
	print(l)
		
		

