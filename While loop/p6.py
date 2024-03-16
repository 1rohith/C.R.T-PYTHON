#take a number input from user check if the sum of factors of that numberis greater than the original number or not
#if yes print yes else no
n=int(input("Enter the number:"))
sum=0
for i in range(1,n/2):
        if n%i==0:
            sum=sum+i
if sum>n:
      print("abundant")
else:
      print("no")