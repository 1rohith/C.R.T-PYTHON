x=int(input("Enter no of rows:"))
#y=int(input("Enter no of columns:"))

for i in range(1,x):
    for s in range(1,x-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()