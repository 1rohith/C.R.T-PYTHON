#write a recursive func to calculate the sum of digits of a number

def sum(n):
    sum=0
    if n==0:
        return
    else:
        digit=n%10
        s1=sum+digit
        n=n//10
    return sum(s1)

sum(n)