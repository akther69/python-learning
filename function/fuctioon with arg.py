#positional arguments
# def add(a,b):
#     sum=a+b
#     print(sum)
# add(3,5)
# add(8,9)


#create a function circle and pass radius as argument find area
# def cricle_area(r):
#     area=(22/7)*r**2
#     print(area)
# cricle_area(10)
# cricle_area(11)


#1.create a function multiplication with single positional arg and generate multiplication table of the num
# def multiplication(num):
#     for i in range(1,11):
#         print(num,"*",i,"=",num*i)
# multiplication(5)
#
#
# #2.find the factorial  of a number passing into a function
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     print("factorial of",num,"is",fact)
# factorial(5)
#
#
# #3.find the largest of 3 number passing into a function
# def larg_Three(a,b,c):
#     if(a>b and a>c):
#         print(a,"is greater")
#     elif(b>c):
#         print(b,"is greater")
#     else:
#         print(c,"is greater")
# larg_Three(2,1,4)
# larg_Three(9,2,1)
#
#
# #4 find the reverse of a string passing into a function
# def reverse(a):
#     rev=""
#     for i in str(a):
#         rev=i+rev
#     print(rev)
# reverse("akther")
#
#
# # 5.create a function to check a number is palindrome or not
# def palindrome(a):
#     pali=""
#     copy=str(a)
#     for i in copy:
#         pali=i+pali
#     if(pali==copy):
#         print(a,"is palindrome")
#     else:
#         print(a,"is not palindrome")
# palindrome("malayalam")
# palindrome("akther")
# palindrome(1001)
#
#
# # 6.remove vowels from a string passing into a function
# def remove_vowels(a):
#     no_vowel=""
#     for i in a:
#         if((i=="a") or (i=="e") or (i=="i") or (i=="o") or (i=="u")):
#             continue
#         else:
#             no_vowel+=i
#     print(no_vowel)
# remove_vowels("akther")
# remove_vowels("aeioufgfgfgfg")






#Arbitary arguments
# if you don"t no how many arguments that are passed into an function add * before the argument

# def add(*num):
#     sum=0
#     for i in num:
#         sum+=i
#     print("The sum is =",sum)
# add(1,2,3,4,5,6,7,8,9)
# add(10,5)
# add(8.2,1)

#q1 create a function product with arbitary
# def product(*num):
#     product=1
#     for i in num:
#         product*=i
#     print("the product is",product)
# product(1,2,3,4)
# product(8,5)


# #q2 create a function with min_value()
# def min_value(*num):
#     min=num[0]
#     for i in num:
#         if (i<min):
#             min=i
#     print("The smallest value is",min)
# min_value(1,2,3)
# min_value(10,66,9)
#
#
# #q3 create a fn max_value
# def max_value(*num):
#     max=num[0]
#     for i in num:
#         if (i>max):
#             max=i
#     print("The largest value is",max)
# max_value(1,2,3)
# max_value(10,66,9)


#q4 rev_str()
# def rev_str(*str):
#     for i in str:
#         reverse=""
#         for j in i:
#             reverse=j+reverse
#         print(i,":",reverse)
# rev_str("hai","hellow")




#default arguments
#default arguments are the values that will be used if no arguments passed into function during function call
# def add(a,b,c=0):
#     sum=a+b+c
#     print(sum)
# add(1,2)
# add(1,3,5)


#q1 create a function largest using default argument method
# def largest(a,b=0,c=0):
#     if(a>b and a>c):
#         print(a,"is largest")
#     elif(b>c):
#         print(b,"is largest")
#     else:
#         print(c,"is largest")
# largest(1,2)
# largest(1,3,5)
# largest(6)



#keyword arguments are the values that are passed into the function are identifiable by the specific parameter name
# def name(firstname,lastname,middlename):
#     print("firstname=",firstname,"lastname=",lastname,"middlename=",middlename)
# name(lastname="s",firstname="suhaib",middlename="akther")



#Arbitary keyword arguments: if you dont no how many key values pair that are passing into a function put ** before the arguments
# def reg(**kwarg):
#     print(kwarg)
# reg(firstname="suhaib",secondname="akther",phoneno=7598488180)


#create a function that passes key value pairs and finally print key and value separately
# def reg(**kwargs):
#     for i,j in kwargs.items():
#         print(i,"=",j)
# reg(firstname="suhaib",secondname="akther",email="ssuahaddhkfdhi@gmail.com",phone=7598488180)


# def reg(**kwargs):
#     for i,j in kwargs.items():
#         print(i,"=",j)
# reg(firstname="suhaib",secondname="akther",email="ssuahaddhkfdhi@gmail.com",phone=7598488180)


#pass given key value pair into the fn and finally print the sorted dictionary
# def soort(**dic):
#     srt={}
#     l=list(dic)
#     l.sort()
#     for i in l:
#         srt[i]=dic[i]
#     print(srt)
# soort(a=1,k=5,c=3,d=4)


# def quad(a,b,c):
#     d=(b**2-4*a*c)**0.5
#     x1=(-b+d)/(2*a)
#     x2=(-b-d)/(2*a)
#     return "%s %s"%(x1,x2)
# print(quad(1,4,-12))


