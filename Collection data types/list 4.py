l=[2,0,1024,0,40,230,0]
#shift all the zeros to right.
l1=[0]
for i in range(len(l)):
    if l[i]!=0:
        l1=l[i]
        print(l1,end=" ")
for i in range(len(l)):
    if l[i]==0:
        l1=l[i]
        print(l1,end=" ")