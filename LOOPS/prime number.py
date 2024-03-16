#n=13
flag=0
n=int(input("Enter the number:"))
for i in range(2,n/2):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("Not a prime")
else:
    print("Prime")
