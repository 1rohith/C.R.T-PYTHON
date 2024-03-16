"""#toyota
#mahindra
#mercedes
#take the input from user for the car company name and in the input message  give the user the 3 options of the 
company.This user input company name  goes as the input/argument to model name function,which welcomes the user 
accordingly to the company name. Ask the user to enter the specific model name for that company(gns,gdi etc..)
The second function whose name is variant. According to the car company name and car model the user should be asked
to enter the variant he would like to choose from petrol,diesel. Display function according to the car company name
and car model name and car variant first its ex showroom price should be displayed and then its onroad price should 
be displayed,which is calculated as ex showroom price+ cgst+ sgst+ insurance."""

class carshowroom:
    def __init__(self):
        self.cars=[]
    def modelname(self, company):
        print("Welcome to {company} family!")
        model=input("Enter the model name for {company}:")
        return model
    def variant(self, company, model):
        print("select the variant for {company} {model}")
        var=input("Enter the variant from below:\n 1.Petrol\n,2.Diesel\n")
        return var
    #def display(self,company,model,variant):



#user input
company=input("Enter the company name(1.Toyota, 2.Mahindra, 3.Mercedes):")
#obj creation
sr=carshowroom()
sr.modelname(company)
sr.variant(company,model)


