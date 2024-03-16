#1578= 1^1+5^2+7^3+8^4

#armstrong number - sum of  numbers with the number of digits as power for individual numbers

n=int(input("Enter the number:"))
n1=n
org=n
count=0
sod=0

while(n>0):
    count=count+1
    n=n//10
while(n1>0):
    digit=n1%10
    sod=sod+digit**count
    n1=n1//10
    count=count-1
print(sod)

if sod==org:
    print("armstrong")
else:
    print("no")

    