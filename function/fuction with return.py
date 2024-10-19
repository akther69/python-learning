#function with return type
#the python return statement which is used to return an output from an function
#a program have only one return active at a time
# def add(a,b):
#     return a+b
# print(add(3,6))


#q1 find the largest of two number into a fn using fn with return type
# def  larg(a,b):
#     if(a>b):
#         return "%d is greater"%a
#     elif(a==b):
#         return "%d is equal to %d"%(a,b)
#     else:
#         return "%d is greater"%b
# print(larg(5,6))
# print(larg(6,6))


# formators
# %s=string
# %d=integers numbers
# %f=float numbers
#\n=new line
#\t=tab space


#q1 create a function that passes list as a arguments given list as a argument finally return a list without duplicate value
# def dupli(*string):
#     li=[]
#     for i in string:
#         li.append(i)
#         k=set(li)
#         l=list(k)
#         l.sort()
#     return l
# print(dupli('a','a','b','b'))
