#write a program in which u take an integer input from the user if it is divisible by 3 and 6.print good number 
#if the integer is divisible by 2 and 7 then print an average number
#if the integer is divisible by 4 or 9 then print awesome number, 
#else print bad number

a=int(input("Enter the number:"))

if a%3==0 and a%6==0:
    print("good number")
elif a%2==0 and a%7==0:
    print("average number")
elif a%4==0 or a%9==0:
    print("awesome number")
elif a%2==0 and a%9==0:
    print("m1")
else:
    print("bad number")

