from abc import ABC,abstractmethod
# class vechile(ABC): #abstraction class
#     @abstractmethod
#     def wheel(self):
#         pass
#     @abstractmethod
#     def mirror(self):
#         pass
# class car(vechile):
#     def airbag(self):
#         print("Car have airbag")
#     def wheel(self):
#         print("Car have 4 wheels")
#     def mirror(self):
#         print("Car have two mirror")
# class bike(vechile):
#     def stand(self):
#         print("bike have side stand")
#     def wheel(self):
#         print("bike have wheel")
#     def mirror(self):
#         print("bike have mirrors")
# obj=car()
# obj.airbag()
# obj.wheel()
# obj.mirror()
# print()
# obj1=bike()
# obj1.stand()
# obj1.mirror()
# obj1.wheel()



#in python the pass keyword is null operation it is the placeholder which do noting this are many used when you needs to create empty classes or empty functions
#for absraction we cannot create a object



#create a abstraction base class payment
#payment with abstract
# from abc import ABC,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
# class creditcardpayment(payment):
#     def __init__(self,cardno,cardholder,cvv,expiry_date):
#         self.card_no=cardno
#         self.card_holder=cardholder
#         self.cvv=cvv
#         self.expiry_date=expiry_date
#     def display_details(self):
#         print("Card no=",self.card_no)
#         print("Card holder=",self.card_holder)
#         print("CVV=",self.cvv)
#         print("Expiry date=",self.expiry_date)
#     def pay(self,amount):
#         print("processing credit card payment of $",amount)
# class paypal(payment):
#     def __init__(self,email,password):
#         self.email=email
#         self.password=password
#     def paypal_detail(self):
#         print("Email=",self.email)
#         passw=''
#         for i in self.password:
#             passw+='*'
#         print("Password=",passw)
#     def pay(self,amount):
#         print("processing paypal payment of $",amount)
# obj=creditcardpayment(1234,"suhaib",234,"04/25")
# obj.display_details()
# obj.pay(100)
# print()
# obj1=paypal("suhaib@gmail.com","ak12dc")
# obj1.paypal_detail()
# obj1.pay(1000)