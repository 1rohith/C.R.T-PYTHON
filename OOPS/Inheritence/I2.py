#create a class of name placements which has a function info which displays "No of placements".
#create another class departement with function display which will display the names of departement present in the college.
#create a class pragati with a function welcome which displays the message "Welcome to pec college" 
#and this pragati class should also displays details about departements and placements.

#Multiple Inheritence

class Placements:

    def info(self):
        print("The Number of placements in the year 2k24 are 690 and **still counting")
    
class Departement(Placements):
    def display(self):
        #self.dept=departement
        print("The departements are:\n ece\n cse\n mech\n eee\n ds\n ai\n aiml")

class Pragati(Departement):
    def welcome(self):
        print("Welcome to P.E.C")

obj=Placements()
obj.info()
obj1=Departement()
obj1.display()
obj2=Pragati()
obj2.welcome()
