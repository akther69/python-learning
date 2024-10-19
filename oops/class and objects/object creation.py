# it is key which is used to making data public or private
# class laptop:
#     def setvalue(self,brand_name,processor,ram,colour):
#         self.brand=brand_name
#         self.pro=processor
#         self.ram=ram
#         self.colour=colour
#     def printval(self):
#         print("brand name=",self.brand)
#         print("processor=",self.pro)
#         print("ram=",self.ram)
#         print("colour=",self.colour)
# obj=laptop()
# obj.setvalue(brand_name="HP",ram="8gb",processor="intel",colour="white")
# obj.printval()



#create a class bank
#create a function user detail:username,account number,email
#create a function view details:display the user details
# create a function depsit(amount)
#withdraw(amount)
# class bank:
#     def userdetail(self,username,account_number,email):
#         self.username=username
#         self.acntno=account_number
#         self.email=email
#         self.balance=0
#     def viewdetail(self):
#         print("username=",self.username)
#         print("account number=",self.acntno)
#         print("email=",self.email)
#     def deposit(self,a):
#         self.balance+=a
#         print("Deposit=",self.balance)
#     def withdraw(self,a):
#         if(a<=self.balance):
#             self.balance-=a
#             print("Final balance",self.balance)
#         else:
#             print("Insufficient balance cannot withdraw")
# obj=bank()
# obj.userdetail(username="suhaib",account_number="22234A",email="ssuhaib@gmail.com")
# obj.viewdetail()
# obj.deposit(1000)
# obj.withdraw(1001)


#create a class student with method
#student_details():id,name,dept,maths,phy,chem
#total_mark():math+phy+chem
#display() student_details
#create 3 student object
# class student:
#     def student_details(self,id,name,dept,maths,phy,chem):
#         self.id=id
#         self.name=name
#         self.department=dept
#         self.maths=maths
#         self.physics=phy
#         self.chemistry=chem
#         self.total=0
#     def total_mark(self):
#         self.total=self.maths+self.physics+self.chemistry
#         print("total mark=",self.total)
#     def display(self):
#         print("id=",self.id)
#         print("name=",self.name)
#         print("department=",self.department)
#         print("maths mark=",self.maths)
#         print("physics mark=",self.physics)
#         print("chemistry mark",self.chemistry)
# obj1=student()
# obj1.student_details(id='10001',name="suhaib",dept="cse",maths=77,chem=88,phy=99)
# obj1.display()
# obj1.total_mark()
# obj2=student()
# obj2.student_details(1002,"akther","cse",77,77,77)
# obj2.display()
# obj2.total_mark()
# obj3=student()
# obj3.student_details(1003,"rambo","cse",77,100,100)
# obj3.display()
# obj3.total_mark()



