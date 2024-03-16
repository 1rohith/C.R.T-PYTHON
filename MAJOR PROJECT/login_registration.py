import csv
class Reg_log:
    def registration(self,username,password,phone_no,pin,city):
        self.u_name=username
        self.pwd=password
        self.ph_no=phone_no
        self.pincode=pin
        self.n_city=city
        #print("Register Yourself:")  
        with open("randl.csv","a",newline="") as file:
            store=csv.writer(file)
            store.writerow([self.u_name,self.pwd,self.ph_no,self.pincode,self.n_city])
            print("Registration Successful!")
            print("Log in using your credentials")
    def login(self,username,password):
        with open("randl.csv","r",newline="") as file:
            read=csv.DictReader(file)
            for row in read:
                if row["u_name"]==username and row["pwd"]==password:
                    print("Login Successful")
                    return True
        
        return False
                     



