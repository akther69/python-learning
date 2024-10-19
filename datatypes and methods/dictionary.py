person={"name":"suhaib","age":21,"phone":98765432}
# print(person)
# print(type(person))
# print(person.keys())
# print(person.values())
# print(person.items())  #pair
#
#
# #get it is used to access value using key
# print(person.get("name"))
#
#
# #len
# print(len(person))
#
# #update
# person.update({"email":"ssuhaibakther12@gmail.com"})
# print(person)
#
# person.update({"phone":7598488180})
# print(person)
#
# #dictionary is unindexed it is not possible to take in index
#
#
# #without using update method
# person["name"]="akther"
# print(person)
#
#
# #pop()
# # person.pop("age")
# # print(person)
#
#
# person.popitem()
# print(person)
#
#
# person["fullname"]=person.pop("name")
# print(person)
#
#
# #dictionary iteration
# for i in person:
#     print(i)
#
#
# for i in person.values():
#     print(i)
#
#
# for i in person.keys():
#     print(i)
#
#
# for i,j in person.items():
#     print(i,j)
#
#
#write a program to create a dictionary
# pair=int(input("Enter the number of pair: "))
# dic={}
# for i in range(pair):
#     key=input("Enter the key: ")
#     values=input("Enter the keys: ")
#     if(values.isdigit()):
#         dic.update({key:int(values)})
#     elif(values.isalpha()):
#         dic.update({key:values})
#     elif isinstance(float(values),float):
#         dic.update({key:float(values)})
# print(dic)

#Qst
# pair=int(input("Enter the number of pair: "))
# dic={}
# for i in range(pair):
#     key=input("Enter the element: ")
#     dic.update({key:len(key)})
# print(dic)


#create a dictionary input by the user
# pair=int(input("Enter the element: "))
# dic={}
# for i in range(pair):
#     key=int(input("enter the value: "))
#     if(key%2==0):
#         dic.update({key:"even"})
#     else:
#         dic.update({key:"odd"})
# print(dic)


#task dictionary sorting
# num={"b":2,"a":1,"d":4,"c":3}
# d={}
# k=list(num)
# k.sort()
# print(k)
# for i in k:
#     d.update({i:num.get(i)})
# print(d)


#sorted
# num={"b":2,"a":1,"d":4,"c":3}
# d=dict(sorted(num.items()))
# print(d)