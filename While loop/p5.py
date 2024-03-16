#take an integer as an input from the user and check whether if the number is divisible by its sum of digits or not
n=int(input("Enter the number:"))
n1=n
sum=0
while(n>0):
    digit=n%10
    sum=sum+digit
    n=n//10
if n1%sum==0:
    print("harshad number")
else:
    print("no")