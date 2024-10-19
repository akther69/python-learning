#HIERARCHICAL INHERITANCE
#it is inheritance in which parent class is inherited by many sub class
#Without using constructor
# class data:
#     def data_deatails(self,name,gender,phone):
#         self.name=name
#         self.gender=gender
#         self.phone=phone
#     def data_display(self):
#         print("Name=",self.name)
#         print("Gender=",self.gender)
#         print("Ph no=",self.phone)
# class doctor(data):
#     def doctor_details(self,hospital_name,specification):
#         self.hospital_name=hospital_name
#         self.specification=specification
#     def doctor_display(self):
#         print("Name=", self.name)
#         print("Gender=", self.gender)
#         print("Ph no=", self.phone)
#         print("Hospital Name=",self.hospital_name)
#         print("Specification=",self.specification)
# class engineer(data):
#     def engineer_details(self,company_name,designation):
#         self.company_name=company_name
#         self.designation=designation
#     def engineer_display(self):
#         print("Name=", self.name)
#         print("Gender=", self.gender)
#         print("Ph no=", self.phone)
#         print("Company Name=",self.company_name)
#         print("Designation=",self.designation)
# obj1=doctor()
# obj1.data_deatails("suhaib","male",75987566744)
# obj1.doctor_details("appolo","cardio")
# obj1.doctor_display()
# print()
# obj2=engineer()
# obj2.data_deatails("ameen","male",75234567)
# obj2.engineer_details("tcs","Developer")
# obj2.engineer_display()


#with using constructor
# class data:
#     def __init__(self,name,gender,phone):
#         self.name=name
#         self.gender=gender
#         self.phone=phone
#     def data_display(self):
#         print("Name=",self.name)
#         print("Gender=",self.gender)
#         print("Ph no=",self.phone)
# class doctor(data):
#     def __init__(self,name,gender,phone,hospital_name,specification):
#         data.__init__(self,name,gender,phone)
#         self.hospital_name=hospital_name
#         self.specification=specification
#     def doctor_display(self):
#         print("Name=", self.name)
#         print("Gender=", self.gender)
#         print("Ph no=", self.phone)
#         print("Hospital Name=",self.hospital_name)
#         print("Specification=",self.specification)
# class engineer(data):
#     def __init__(self,name,gender,phone,company_name,designation):
#         data.__init__(self,name,gender,phone)
#         self.company_name=company_name
#         self.designation=designation
#     def engineer_display(self):
#         print("Name=", self.name)
#         print("Gender=", self.gender)
#         print("Ph no=", self.phone)
#         print("Company Name=",self.company_name)
#         print("Designation=",self.designation)
# obj1=doctor("suhaib","male",7543567334,"Appolo","Cardio")
# obj1.doctor_display()
# print()
# obj2=engineer("akther","male",987654789,"Tcs","developer")
# obj2.engineer_display()