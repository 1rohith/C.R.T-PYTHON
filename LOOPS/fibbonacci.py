#fibbonacci series 
#0 1 1 2 3 5 8 13 21 34 ...
a=0
b=1
print(a)
print(b)
for i in range(8):
    temp=a+b
    print(temp)
    a=b
    b=temp
  