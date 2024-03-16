#collection data types
#creating
list=["Hyna",12.4,"gna",10,15,"nvidia","blueberg"]

#access
print(list)

#slicing
print(list[0:3])
print(list[0:-1])
print(list[:2:6])
print(list[:4])
print(list[0:6:2])
print(list[:-1])

#updating
list[2]="tree"
print(list)

#append
list.append("kashmir")
print(list)

#remove
list.remove("blueberg")
print(list)

#update
list[3]=32
print(list)

#loops
for i in list:
    print(list)

#insert
list.insert(2,"rohith")
print(list)



