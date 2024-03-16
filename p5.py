#write a program to check the onroad price of a bike under the conditions 
#if the price is greater than 72000 then  tax is 10% of actual price and insurance will be 15% of actual price
#if the price is greater than 150000 and less than 200000 the tax would be 25% and insuerance will be 20%
#if the price is above 200000 then tax will be 35% and insurance will be 28%
#otherwise print valid amount
#actual price+tax+insurance = onroad price

a=int(input("Enter the price of a bike:"))

if a>72000 and a<150000:
    tax=(a*10)/100
    insurance=(a*15)/100
    onroad=a+tax+insurance
    print("onroad price:",onroad)
elif a>150000 and a<200000:
    tax=(a*25)/100
    insurance=(a*20)/100
    onroad=a+tax+insurance
    print("onroad price:",onroad)
elif a>200000:
    tax=(a*35)/100
    insurance=(a*28)/100
    onroad=a+tax+insurance
    print("onroad price:",onroad)
else:
    print("enter a valid price")