#Main function
import login_registration
class m:
    def __init__(self):
        #self.r_l=Reg_log()
        pass

    def registration(self):
        username=input("Enter your name:")
        password=input("Enter a strong password:")
        phone_no=int(input("Enter your mobile number:"))
        pin=int(input("Enter your city pin code:"))
        city=input("Enter your city name:")
        login_registration.Reg_log.registration(self,username,password,phone_no,pin,city)
    def login(self):
        username=input("Enter your name:")
        password=input("Enter your password:")
        login_registration.Reg_log.login(self,username,password)

obj=m()
obj.registration()
obj.login()