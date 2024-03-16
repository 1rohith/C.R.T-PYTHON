#reversing the given number
n=int(input("Enter the number:"))

while(n>0):
    digit=n%10
    print(digit,end=" ")
    n=n//10

