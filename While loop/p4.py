#multiplication of digits
n=int(input("Enter the number:"))
mul=1

while(n>0):
    digit=n%10
    mul=mul*digit
    n=n//10
print(mul)