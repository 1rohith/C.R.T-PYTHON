#number of digits 
n=int(input("Enter the number:"))

count=0
while(n>0):
    digit=n%10
    n=n//10
    count=count+1
print(count)