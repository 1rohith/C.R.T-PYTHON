#creating a csv file by adding data
import csv
s=open("stu.csv","a",newline="")
a=csv.writer(s) #
a.writerow(["S_Name","S_id","Mobile_no","Branch"])
for i in range(2):
    S_Name=input("Enter student name:")
    S_id=int(input("Enter student id:"))
    Mobile_no=int(input("Enter number:"))
    Branch=input("Enter branch name:")

    a.writerow([S_Name,S_id,Mobile_no,Branch])
    print("records have been saved")


with open("stu.csv","r",newline="") as file:
    read=csv.DictReader(file)
    #store=csv.writer(file)
    #for row  in read:
        #if row["S_name"]==
    print(read)
