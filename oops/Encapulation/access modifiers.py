#ACCESS MODIFIER IN ENCAPULATION
#in oops access modifier is used to limit the access to the variables and the functions of a class

    #Types
    #PUBLIC ACCESS MODIFIERS:
        #Accessible from anywhere from outside the class
    #PRIVATE ACCESS MODIFIERS:
        #Accessible within the class
    #PROTECTED ACCESS MODIFIERS:
        #Accessible within the class and its sub classes


# class encapulation:
#     def __init__(self,name,salary,project):
#         self.name=name
#         self.__salary=salary
#         self._project=project
#     def __display(self): #private method


#PUBLIC ACCESS MODIFIER
# class person:
#     def __init__(self,name,salary,project):
#         self.name=name
#         self.salary=salary
#         self.project=project
#     def display(self):
#         print("name=",self.name)
#         print("salary=", self.salary)
#         print("project=", self.project)
# obj=person("suhaib",13000,"ecommerce")
# obj.display()
# print()
# print(obj.name)
# print(obj.salary)
# print(obj.project)
# print()
# obj.name="akther"
# obj.salary=123434
# obj.project="new project"
# obj.display()



#PRIVATE ACCESS MODIFIER
# class person:
#     def __init__(self,name,salary,project):
#         self.name=name
#         self.__salary=salary
#         self.__project=project
#     def display(self):
#         print("name=",self.name)
#         print("salary=", self.__salary)
#         print("project=", self.__project)
# obj=person("suhaib",13000,"ecommerce")
# print(obj.name)
# print(obj.salary)  #not accessible outside the class
# print(obj.project) #not accessible outside the class
# obj.display()


#NAMEMANGLING
#it is the method: it is used to access the private data member or method inside a class


#syntax
# _classname__datamember
class person:
    def __init__(self,name,salary,project):
        self.name=name
        self.__salary=salary
        self.__project=project
    def __display(self):
        print("name=",self.name)
        print("salary=", self.__salary)
        print("project=", self.__project)
obj=person("suhaib",13000,"ecommerce")
print(obj.name)
print(obj._person__salary)  #not accessible outside the class
print(obj._person__project)
# obj._person__display()