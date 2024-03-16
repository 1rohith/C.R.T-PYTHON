#reverse using recursion
def rev(n):
    #nod=0
    if n==0:
        return 
    print(n%10)
    return rev(n//10)
rev(12)
           

   
        