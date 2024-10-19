#it is type of inheritance that inherits a class that has already inherited some other class
# without using constructor
# class mobile:
#     def mobile_details(self,storage,brand):
#         self.storage=storage
#         self.brand=brand
#     def mobile_display(self):
#         print("Storage=",self.storage)
#         print("Brand=",self.brand)
# class sumsung(mobile):
#     def sumsung_details(self,model,price):
#         self.model=model
#         self.price=price
#     def sumsung_display(self):
#         print("Model=",self.model)
#         print("Price=",self.price)
# class galaxy(sumsung):
#     def galaxy_details(self,colour,processor,ram):
#         self.colour = colour
#         self.processor=processor
#         self.ram=ram
#     def galaxy_display(self):
#         print("Storage=", self.storage)
#         print("Brand=", self.brand)
#         print("Model=", self.model)
#         print("Price=", self.price)
#         print("Colour=",self.colour)
#         print("Processor=",self.processor)
#         print("Ram=",self.ram)
# obj=galaxy()
# obj.galaxy_details("blue","snapdragon","8GB")
# obj.mobile_details(128,"galaxy")
# obj.sumsung_details("galaxy121",25000)
# obj.galaxy_display()


#with using constructor
# class ceo:
#     def __init__(self,company_name,ceo_name):
#         self.company_name=company_name
#         self.ceo_name=ceo_name
#     def ceo_display(self):
#         print("Company name=",self.company_name)
#         print("Ceo name=",self.ceo_name)
# class manager(ceo):
#     def __init__(self,company_name,ceo_name,manager_name,department,designation):
#         ceo.__init__(self,company_name,ceo_name)
#         self.manager_name=manager_name
#         self.department=department
#         self.designation=designation
#     def manager_display(self):
#         print("Manger name=",self.manager_name)
#         print("Department=",self.department)
#         print("Designation=",self.designation)
# class employee(manager):
#     def __init__(self,company_name,ceo_name,manager_name,department,designation,employee_name,emp_id):
#         manager.__init__(self,company_name,ceo_name,manager_name,department,designation)
#         self.employee_name=employee_name
#         self.emp_id=emp_id
#     def employee_display(self):
#         print("Company name=", self.company_name)
#         print("Ceo name=", self.ceo_name)
#         print("Manger name=", self.manager_name)
#         print("Department=", self.department)
#         print("Designation=", self.designation)
#         print("Employee Name=",self.employee_name)
#         print("Employee id=",self.emp_id)
# obj=employee("luminar","arjun","arun","it","Developer","suhaib","71626")
# obj.employee_display()
# print()
# obj.manager_display()
# print()
# obj.ceo_display()