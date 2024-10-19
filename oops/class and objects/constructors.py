#CLASS CONSTRUCTORS
    # __init__()
# it is a special method inpython which is used for initializing new object
# it is called automatically when new instance of class is created
# class vechile:
#     def __init__(self,name,model,regno,price):
#         self.name=name
#         self.regno=regno
#         self.model=model
#         self.price=price
#     def display(self):
#         print("Vehicle Name=",self.name)
#         print("regno=",self.regno)
#         print("model=",self.model)
#         print("price=",self.price)
# obj=vechile("maruthi","Alto","KL10M1249","50000")
# obj.display()


#create a class product using constructor
#productname,price,quantity
#display product price quantity total amount ordered date
#delivary_details()
#prodname,price,estimated delivery date

# class product:
#     ecommerce="Flipkart"
#     def datetime(self):
#         import datetime
#         from datetime import timedelta
#         d=datetime.date.today()
#         d+=timedelta(days=10)
#         print(d)
#         today = datetime.date.today()
#         print(today)
#     def __init__(self,prodname,price,quantity):
#         self.prodname=prodname
#         self.price=price
#         self.quantity=quantity
#         self.total_amount=0
#         import datetime
#         today = datetime.date.today()
#         self.ordered_date=today
#     def display(self):
#         print("product name=",self.prodname)
#         print("Price=",self.price)
#         print("Quantity=",self.quantity)
#         print("Total amount=",self.total_amount+(self.price*self.quantity))
#         print("Ordered date=",self.ordered_date)
#     def delivary_details(self):
#         print('Product name=',self.prodname)
#         print("Total amount=", self.total_amount + (self.price * self.quantity))
#         # print("price=",self.price)
#         import datetime
#         from datetime import timedelta
#         d = datetime.date.today()
#         d += timedelta(days=10)
#         print("Estimated delivary date=",d)
#
# obj=product("bag",500,3)
# obj.display()
# print()
# obj.delivary_details()
