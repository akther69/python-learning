list=["suhaib","male",35,35,21]
# # print(list)
# # print(type(list))


# #append():it is used to add at the end
# list.append("akther")
# print(list)


# #insert():it is used to add the element to the specific position
# list.insert(0,"shajahan")
# print(list)


# #extend()
# list1=["shajimma","paapa",12,34]
# list.extend(list1)
# print(list)


# #pop()
# list.pop()#it is used to delete the last element
# print(list)
# list.pop(5)#it is used to delete the specific element
# print(list)


# #remove():it is used to delete the element by the name
# list.remove("suhaib")
# print(list)


# #reverse()
# list.reverse()
# print(list)


# # count()
# print(list.count(35))


# #sort()
# names=["suhaib","delwin","shehjas","agnal"]
# names.sort(reverse=True)
# print(names)


# #slicing
# print(names[0:3])
# print(names[::-1])


# #list iteration
# li=['a','b','c']
# for i in li:
#     print(i)


#q1 find the length of the string without using len()
#q2 find the sum of the element in the given list
#q3 write a program to find the count of numbers and alphabets in the given list l=["a",'b',1,2,'c','d',3,4]
# #q1
# a=['a','b',1,2,3,4,4]
# length=0
# for i in a:
#     length+=1
# print(length)


#q2
# a=[100,200,300,400]
# sum=0
# for i in a:
#     sum+=i
# print("sum= ",sum)


#q3
# l=["a",'b',1,2,'c','d',3,4,5,9,8]
# alphabets=0
# number=0
# for i in l:
#     if(str(i).isalpha()):
#         alphabets+=1
#     elif(str(i).isdigit()):
#         number+=1
# print("alphabet=",alphabets)
# print("num=",number)


# list=[]
# a=int(input("Enter the number = "))
# for i in range(a):
#     inside=input("Enter the list= ")
#     if(inside.isdigit()):
#         list.append(int(inside))
#     elif (inside.isalpha()):
#         list.append(inside)
#     elif isinstance(float(inside),float):
#         list.append(float(inside))
#     elif isinstance(float(inside))
# print(list)


# write a program to find the largest element in the given numbers
# list=[5,1,3,2,4]
# greater=[]
# list.sort()
# print("The smallest value is",list[0])
# list.sort(reverse=True)
# print("The largest value is",list[0])

# list=[5,1,3,2,4]
# firstvalue=list[0]
#
# for i in list:
#     if(i>firstvalue):
#         firstvalue=i
# print("The greatest value is ",firstvalue)
# for i in list:
#     if(i<firstvalue):
#         firstvalue=i
# print("The smallest value is ",firstvalue)


#wtite a program to remove duplicate elements in the given list
# li=["a","b","a","b","c"]
# repeat=[]
# for i in li:
#     if(i not in repeat):
#         repeat.append(i)
#     else:
#         continue
# print(repeat)


#q2
# names=["akhil","arun","akshay"]
# for i in names:
#     print(i,":",len(i))

#find the largest string
# names=["z","z","zz"]
# firstvalue=names[0]
# for i in names:
#     if(i>firstvalue):
#         firstvalue=i
# print(i,":",len(i))