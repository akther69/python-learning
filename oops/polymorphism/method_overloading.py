#SAME FUNCTION NAME WITH DIFFERENT NUMBER OF PARAMETER AND ARGUMENTS
# class Maths:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj=Maths()
# obj.add(1,2)
# obj.add(1,2,3)

#MULTIPLE DISPATCH  
# in python we cannot achieve method overloading directly but we can implement a method multiple dispatch method to achieve method overloading in python
#step 1: install multipledispatch package
#multipledispatch is an external package we need to install it by using the command pip install multipledispatch

# from multipledispatch import dispatch
# class Maths:
#     @dispatch(int,int)
#     def add(self,a,b):
#         print(a+b)
#     @dispatch(int,int,int)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj=Maths()
# obj.add(1,2)
# obj.add(1,2,3)


#create overloading function length?
# length('hello')
# length([1,2,3,4])
# length((1,2,3,4))
# length({1,2,3,4})
# from multipledispatch import dispatch
# class length:
#     @dispatch(str)
#     def length(self,s):
#         print(len(s))
#     @dispatch(list)
#     def length(self,l):
#         print(len(l))
#     @dispatch(tuple)
#     def length(self,t):
#         print(len(t))
#     @dispatch(set)
#     def length(self,st):
#         print(len(st))
# obj=length()
# obj.length([1,2,3,4])
# obj.length("hellow")
# obj.length({1,2,3,4})
# obj.length((1,2,3,4,8))