#write a program to accept one subject marks from users and check if the marks are greater than 35 print cheated
#if equls to 35 print passed
#if less than 35 failed
marks=int(input("Enter the marks of math:"))

if marks>35:
    print("cheated")
elif marks==35:
    print("passed")
else:
     print("failed")