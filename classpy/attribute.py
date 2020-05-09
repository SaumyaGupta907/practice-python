#hasattr(),getattr(),setattr() and delattr()
class VJIT:
	cse=240
	ece=240
	me=240
	it=60
	eee=120
	ce=120
	ai=60
	def display(self):
		print("College: Vidya jyothi insitute of technology")
		print("CSE intake:240")
		print("ECE intake:240")
		print("ME intake:240")
		print("IT intake:60")
		print("EEE intake:120")
		print("CE intake:120")
		print("AI intake:60")
ob1=VJIT()
print("intake of civil engineering is",getattr(ob1,"ce",0))
print("intake of chemical engineering is",getattr(ob1,"che",0))
#print("intake of chemical engineering is",getattr(ob1,"che"))
print(hasattr(ob1,"ae"))
print("Intake of IT:",getattr(ob1,"it"))
setattr(ob1,"it",180)
print("Intake of IT after upate:",getattr(ob1,"it"))
setattr(ob1,"mba",60)
#print("intake of mba is:",getattr(ob1,"mba"))
