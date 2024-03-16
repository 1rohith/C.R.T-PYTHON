"""#car showroom
#toyota
#mahindra
#mercedes
#take the input from user for the car company name and in the input message  give the user the 3 options of the company
this user input company name  goes as the input/argument to model name function,which welcomes the user accordingly
to the company name. ask the user to enter the specific model name for that company(gns,gdi etc..)
The second function whose name is variant. according to the car company name and car model the user should be asked
to enter the variant he would like to choose from petrol,diesel.
display function according to the car company name and car model name and car variant first its ex showroom price 
should be displayed and then its onroad price should be displayed,which is calculated as 
ex showroom price+ cgst+ sgst+ insurance.
The sgst,cgst, and the insurance all the three have a common value through out the car showroom.
if the user car choice is not present it should print invalid
company name and option also should work
"""

class carshowroom:
    def __init__(self):
        print("")
    def modelname(self,):
        self.co_name=cname
        if n==l[n]:
            print("Welcome to",n,"Family")
        else:
            print("invalid")

n=input("Enter company name from below list of items:\n 1.Toyota\n 2.Mahindra\n 3.Mercedes\n")
obj=carshowroom("Toyota","Mahindra","Mercedes")
obj.modelname(l[n])