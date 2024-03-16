#Overriding - run time
class father:
    def bike(self):
        print("R15")
    def car(self):
        print("Bentley")
class Rohith(father):
    def bike(self):#method overriding
        print("Harley Davidson")

o=Rohith()
o.bike()
o.car()