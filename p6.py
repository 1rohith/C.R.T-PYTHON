#check in if a given year is leap year or not, the conditions are as follows
#if the year is divisible by 4 and not divisible by 100 or if it is divisible by 400 then it is called leap year

year=int(input("Enter the year:"))

if year%4==0 and year%100!=0 or  year%400==0:
      print("It is a leap year")
else:
      print("not a leap year")