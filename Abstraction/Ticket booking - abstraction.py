#create a class ticket which will be the abstract class 
#inside that create a function book ticket which will be the abstract method and has nothing in it.
#create a class makemytrip which will use the bookticket function from ticket class to take the details such as 
#name, ph no, email id,journey date and displays a message saying Thank u for booking from makemytrip.
#create a class irctc which uses the book ticket of ticket class and takes the same details as makemytrip but 
#in the end it will give an option to user to select whether it is one way or round trip.
#if the user option is round trip it again asks the user to enter the return date as well and then prints a message 
#thank u for choosing irctc else it prints a message thank u for choosing irctc.
#create a class indigo which takes all the details as irctc and just asks which mode of transport u want to go in 
#train ,bus or flight and displays a message thank u for choosing indigo

from abc import ABC, abstractmethod
class ticket(ABC):#abstract class
    @abstractmethod
    def bookticket(self):
        pass
class makemytrip(ticket):
    def bookticket(self,name,ph_no,email_id,journey_date):
        self.name1=name
        self.p_no=ph_no
        self.e_id=email_id
        self.j_date=journey_date
        print("Enter the details:",self.name1,self.p_no,self.e_id,self.j_date)
        print("Thank u for booking from makemytrip")
class irctc(ticket):
    def bookticket(self,name,ph_no,email_id,journey_date,j_type):
        self.name1=name
        self.p_no=ph_no
        self.e_id=email_id
        self.j_date=journey_date
        self.jo_type=j_type
        print("Enter the details:",self.name1,self.p_no,self.e_id,self.j_date)
        if self.jo_type=="round trip":
            n=input("Enter the date of return:")
            print("Thank u for choosing irctc")
        else:
            print("Thank u for choosing irctc")
        #print("Enter the details:",self.name1,self.p_no,self.e_id,self.j_date)
        #print("select your desired trip type from below:\n 1.One way\n 2.Round Trip")
class indigo(ticket):
    def bookticket(self,name,ph_no,email_id,journey_date,j_type,mode_transport):
        self.name1=name
        self.p_no=ph_no
        self.e_id=email_id
        self.j_date=journey_date
        self.jo_type=j_type
        self.m_transport=mode_transport

        print("Enter the details:",self.name1,self.p_no,self.e_id,self.j_date)
        if self.jo_type=="One way":
            print("Thank u for choosing irctc")
            if self.m_transport=="train":
                print(" thank u for choosing indigo")
            elif self.m_transport=="bus":
                print(" thank u for choosing indigo")
            elif self.m_transport=="bus":
                print(" thank u for choosing indigo")
        else:
            print("Thank u for choosing irctc")
            if self.m_transport=="train":
                print(" thank u for choosing indigo")
            elif self.m_transport=="bus":
                print(" thank u for choosing indigo")
            elif self.m_transport=="bus":
                print(" thank u for choosing indigo")

obj=indigo()
obj.bookticket("R","9999999","vro")

        
            



