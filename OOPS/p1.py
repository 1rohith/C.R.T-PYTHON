#create a class f15 with functions lights, fan and ac
#lights-when it is called it prints out the color of a light, which is taken as parameter to the function
#fan-when it is called it prints/displays the regulator speed, which is taken as parameter 
#ac diplays the room temperature and the outside  temperature
#write a 4th function whose name is display which displays the difference in outside temperature and room temperature
#and also it displays the fan speed


#constructor is defined like functions but here the function name is defined i.e __init__ 
class f15:
    def __init__(self):#init=initialize
        a=100
        b=10
        #self.a1=a
        #self.b1=b
        print("The placements in P.E.C in 2k24 is",a*b)
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
        print("The difference in temp: ",diff)
        print("The fan speed is:",fs)

obj1=f15()
obj1.light("red")
obj1.fan(40)
obj1.ac(30,40)
obj1.display()



        