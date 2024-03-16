#Multilevel Inheritence

class Placements:

    def info(self):
        print("The Number of placements in the year 2k24 are 690 and **still counting")
    
class Departement():
    def display(self):
        #self.dept=departement
        print("The departements are:\n ece\n cse\n mech\n eee\n ds\n ai\n aiml")

class Pragati(Departement,Placements):
    def welcome(self):
        print("Welcome to P.E.C")

obj=Pragati()
obj.info()
obj.display()
obj.welcome()
