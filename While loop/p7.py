#calculate the difference of
#sum of numbers that are divisible by 6
#and not divisible by 6 in range of first 30 numbers

n=int(input("Enter the number:"))
sum=0
sum1=0
diff=0
for i in range(1,n):
    if(i%6==0):
        sum=sum+i
    else:
        sum1=sum1+i
    diff=sum1-sum
print(diff)
