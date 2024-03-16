#write a program to check the type of triangle where u take the input from the user for 3 sides and
#classify it accordingly by equilateral, isosceles, scaler

a=int(input("Enter the side 1:"))
b=int(input("Enter the side 2:"))
c=int(input("Enter the side 3:"))

if a==b==c:
    print("equilateral")
elif a==b or b==c or a==c:
    print("isosceles")
else:
    print("scaler")