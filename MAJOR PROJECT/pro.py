#products
import csv
class Products:
    def fields(self,name,price,category,stockleft):
        self.p_name=name
        self.p_price=price
        self.p_category=category
        self.stock_left=stockleft
        with open("pro.csv","a",newline="") as file:
            store=csv.writer(file)
            store.writerow([self.p_name,self.p_price,self.p_category,self.stock_left])
            #print("Field has been entered")

        with open("pro.csv","r",newline="") as file:
            read=csv.DictReader(file)
            for row in read:
                print(read)

obj=Products()
obj.fields("Shoes","₹8,000","Fashion","10")
obj.fields("Laptop","₹80,000","Electronics","10")
obj.fields("Matrice","₹1200","Home Appliances","10")
obj.fields("Face wash","₹1,000","Grooming","10")










obj=Products()
obj.fields()
