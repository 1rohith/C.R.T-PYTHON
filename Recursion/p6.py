#write the code of armstrong number using recursion

def cod(n):#12
    if n==0:
        return 0
    return 1+cod(n//10)
#n=int(input("Enter the no:"))
count=cod(153)

def arms(n,c):
    if n==0:
        return 0
    return n%10**c + arms(n//10,c)

