#lists are similar to arrays in c
#however;the list can contain data of different types
#the items stored in the list are separated with a comma(,) and enclosed within square brackets []
#we can use slice operator[:] to access the data of the list
#the concatenation operator(+) and repetition operator(*) works with the list in the same way as they were working with the strings
a= [9,"Hello",2019]
print(a)
print(a[0:2])
print(a+a)
print(a*3)