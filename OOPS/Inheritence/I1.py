#Inheritence
class Faculty:
    def __init__(self,fname,dept,fid):
        self.f_name=fname
        self.f_dept=dept
        self.f_id=fid
    def print_info(self):
        print("Faculty information:",self.f_name,self.f_dept,self.f_id)
obj=Faculty("Ashish","cse",101)
obj.print_info()

class cse(Faculty):
    pass #no statement
obj=cse("Rohith","CSE",109)
obj.print_info()
