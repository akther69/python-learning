#same name with same arguments
#it is used change the behaviour of existing methods and there is a need for at least two classes for method overriding
#in method overriding,inheritance always required as it is done between parent class(super class) and child class(base class)


#overriding in single inheritance
# class maths:#parent class
#     def calculate(self,a,b):
#         print(a+b)
# class maths2:
#     def calculate(self,a,b):
#         print(a*b)
# obj=maths()
# obj.calculate(2,2)
#here maths2 calculate method that overrides the math calculate method


#task
#create a vehicle  class with 2 derived classes car and bike
# class vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def display_details(self):
#         print("Brand=",self.brand)
#         print("Model=",self.model)
# class car(vehicle):
#     def __init__(self,brand,model,num_of_door):
#         vehicle.__init__(self,brand,model)
#         self.num_of_door=num_of_door
#     def display_details(self):
#         print("Brand=", self.brand)
#         print("Model=", self.model)
#         print("Number of door=",self.num_of_door)
# class bike(vehicle):
#     def __init__(self,brand,model,seating_capacity):
#         vehicle.__init__(self,brand,model)
#         self.seating_capacity=seating_capacity
#     def display_details(self):
#         print("Brand=", self.brand)
#         print("Model=", self.model)
#         print("Seating capacity=",self.seating_capacity)
# obj=car("maruthi","alto 800",4)
# obj.display_details()
# print()
# obj=bike("royal enfield","meteor 350",2)
# obj.display_details()