marks= int(input("enter the mark:"))
if marks > 85 and marks <=100:
	print("congrats! you scored grade A")
elif marks > 60 and marks <= 85:
	print("you scored grade B+...")
elif marks > 50 and marks <=60:
	print("you scored grade B")
else:
	print("Fail")