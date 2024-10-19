#SINGLE INHERITANCE
#IT IS A INHERITANCE METHOD IN WHICH A CHILD CLASS THAT INHERIT FROM A SINGLE PARENT CLASS

# class company:
#     def setvalue(self,companyname,location,email):
#         self.companyname=companyname
#         self.location=location
#         self.email=email
#     def display(self):
#         print("company name=",self.companyname)
#         print("location=",self.location)
#         print("email=",self.email)
#
# class employee(company): #employee class that inherits company
#     def employee_details(self,ename,eid,mail,salary):
#         self.ename=ename
#         self.eid=eid
#         self.mail=mail
#         self.salary=salary
#     def employee_display(self):
#         print("employee name=",self.ename)
#         print("id=",self.eid)
#         print("mail=",self.mail)
#         print("salary",self.salary)
#         print("company name=", self.companyname)
#         print("location=", self.location)
#         print("email=", self.email)
# obj=employee()
# obj.setvalue("luminar","kakkanad","luminar@gmail.com")
# obj.employee_details("suhaib",71626,"suhaib@gmail.com",13000)
# obj.employee_display()


#task
# class doctor:
#     def doctor_details(self,doc_name,specification,hospitalname):
#         self.doc_name=doc_name
#         self.specification=specification
#         self.hospitalname=hospitalname
#     def doctor_display(self):
#         print("doctor name",self.doc_name)
#         print("specification=",self.specification)
#         print("hospital name=",self.hospitalname)
# class patient(doctor):
#     def patient_details(self,patient_name,patient_id,age,gender):
#         self.patient_name = patient_name
#         self.patient_id = patient_id
#         self.age = age
#         self.gender = gender
#     def patient_display(self):
#         print("patient name=",self.patient_name)
#         print("patient id=",self.patient_id)
#         print("age=",self.age)
#         print("gender=",self.gender)
#         print("doctor name=", self.doc_name)
#         print("specification=", self.specification)
#         print("hospital name=", self.hospitalname)
# obj=patient()
# obj.doctor_details("kannan","ortho","garden")
# obj.patient_details("suhaib",1234,21,"male")
# obj.patient_display()


#with using constractors
# class company: #parent class
#     def __init__(self,cname,cloc):
#         self.cname=cname
#         self.cloc=cloc
#     def company_display(self):
#         print("company name=",self.cname)
#         print("location=",self.cloc)
# class employee(company): #child class
#     def __init__(self,ename,eid,email,cname,cloc):
#         #super()=which is a method that is used to acces the constructor of a parent to child class
#         super().__init__(cname,cloc)
#         self.ename=ename
#         self.eid=eid
#         self.email=email
#     def emloyee_details(self):
#         print("Employee name=",self.ename)
#         print("Employee id=",self.eid)
#         print("employee emails=",self.email)
#         print("company name=", self.cname)
#         print("location=", self.cloc)
# obj=employee("suhaib",71626,"suhaib@gmail.com","lulu","edapally")
# obj.emloyee_details()


#task
# class doctor:
#     def __init__(self,doc_name,specification,hospitalname):
#         self.doc_name=doc_name
#         self.specification=specification
#         self.hospitalname=hospitalname
#     def doctor_display(self):
#         print("doctor name",self.doc_name)
#         print("specification=",self.specification)
#         print("hospital name=",self.hospitalname)
# class patient(doctor):
#     def __init__(self,patient_name,patient_id,age,gender,doc_name,specification,hospitalname):
#         super().__init__(doc_name,specification,hospitalname)
#         self.patient_name = patient_name
#         self.patient_id = patient_id
#         self.age = age
#         self.gender = gender
#     def patient_display(self):
#         print("patient name=",self.patient_name)
#         print("patient id=",self.patient_id)
#         print("age=",self.age)
#         print("gender=",self.gender)
#         print("doctor name=", self.doc_name)
#         print("specification=", self.specification)
#         print("hospital name=", self.hospitalname)
# obj=patient("suhaib",7125,12,"male","arjun","cardio","appolo")
# obj.patient_display()


#task
#create a parent class vehicle with attributes brand,year
#create a child class carwith attributes,clor and num_of_doors
#create 2 car objects
#complete the program using constructor method?
# class vehicle:
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year
#     def display_vehicle_details(self):
#         print("brand name=",self.brand)
#         print("year=",self.year)
# class model(vehicle):
#     def __init__(self,brand,year,color,num_of_doors):
#         super().__init__(brand,year)
#         self.color=color
#         self.num_of_doors=num_of_doors
#     def display(self):
#         print("color=",self.color)
#         print("No of doors=",self.num_of_doors)
#         print("brand name=", self.brand)
#         print("year=", self.year)
# obj1=model("BMW",20244,"bue",4)
# obj1.display()
# print()
# obj2=model("audi",2024,"green",3)
# obj2.display()


