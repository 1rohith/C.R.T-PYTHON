#parametreized constructor
class s:
    def __init__(self,cst,cet):
        self.clst=cst
        self.clet=cet
        print("class start time is:",cst,"and class end time is:",cet)
    def light(self,color):
        print("The color of light is:",color)
    def fan(self,speed):
        self.sp=speed
        print("The speed of fan is:", speed)
    def ac(self,rt,ot):
        self.room_temp=rt
        self.out_temp=ot
        print("The room temp is:",rt,"and The outside temp is:",ot)
    def display(self):
        diff=self.out_temp-self.room_temp
        fs=self.sp
        t1=self.clst
        t2=self.clet
obj1=s("9 AM","4 PM")
obj1.light("red")
obj1.fan(40)
obj1.ac(30,40)
obj1.display()


