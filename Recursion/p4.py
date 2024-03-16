#write a recursive function to count the no of digits of a number

def cod(n):
    if n==0:
        return 0
    return 1+cod(n//10)
print(cod(1234))