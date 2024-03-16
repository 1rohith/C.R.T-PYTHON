#l=[22,-1,42,65,1,-4,6]
#write a program to find the second smallest negative number from the list without using sort, min, max

#first method
l=[22,-1,42,65,1,-4,6]
mini=999
mini1=999
for i in range(len(l)):
    if mini>l[i]:
        mini=l[i]
print("first smallest neg no:",mini)
for i in range(len(l)):
    if mini1>l[i] and l[i]!=mini:
        mini1=l[i]
print("Smallest neg no:",mini1) 


#2nd method
l=[22,-1,42,65,1,-4,6]
m1=999
m2=999
for i in range(len(l)):
    if l[i]<m1:
        m2=m1
        m1=l[i]
    elif m2>l[i] and m2>m1:
        m2=l[i]
print("Second smallest neg no:",m2)
print("first smallest neg no:",m1)

#3rd method
l=[22,-1,42,65,1,-4,6]
mini=0
for i in range(len(l)):
    if mini>l[i]:
        mini=l[i]
        
        print(mini)
