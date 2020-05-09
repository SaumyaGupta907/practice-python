class Employee:
    basicpay=30000
    hra=4500
    da=1500
    ta=1500
    other=2500
    def __init__(self,name,eid):
        self.name=name
        self.eid=eid
    def grosspay(self):
        self.gross= Employee.basicpay+Employee.hra+Employee.da
        return self.gross
e1= Employee("ABC",4016)
print(hasattr(e1,"name"))
e2= Employee("XYZ",4015)
print(hasattr(e2,"name"))
delattr(e1,"name")
print(hasattr(e1,"name"))
print(hasattr(e2,"name"))
print(hasattr(e1,"other"))
delattr(Employee,"other")
#print(hasattr(e1,"other"))
print(hasattr(e2,"other"))
setattr(e1,"increment",1000)
print(hasattr(e1,"increment"))
print(hasattr(Employee,"increment"))
setattr(Employee,"other1",1000)
print(hasattr(e1,"other1"))
print(hasattr(Employee,"other1"))
print(getattr(e2,"eid"))
print(getattr(Employee,"basicpay"))
print(e1.grosspay())
