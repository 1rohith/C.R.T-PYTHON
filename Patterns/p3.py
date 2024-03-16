n=int(input("Enter the no of rows:"))

for i in range(1,n):
    #spaces
    for s in range(1,n-i):
        print(" ",end=" ")
    for j  in range(1, 2*i):
        print("*",end=" ")
    print()