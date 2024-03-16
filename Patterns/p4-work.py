n=int(input("Enter no of rows:"))

for i in range(1,n):#1
    for s in range(1,n-i):
        print(" ",end=" ")
    for j in range(1,n):#1234
        #if (i==1 or i==n-1 or j==1 or j==n-1):
            print("*", end=" ")
        #else:
            print(" ",end=" ")
    print()