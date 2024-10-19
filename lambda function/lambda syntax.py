# lamba function
# it is anonymous function which means function without names it is typically used for solving short and simple operation
#filter()
#map()
#reduce()


# x=lambda a,b:a+b
# print(x(1,2))
#variable=lambda arguments:expersion


#1find square rooot of the number  passiong into a lambda function
# l=lambda a:a**0.5
# print(l(16))
#
#
# #2 find cube root of the number
# l=lambda a:a**(1/3)
# print(l(8))
#
#
# #find the area of the circle
# l=lambda r:3.14*r**2
# print(l(10))
#
#
# #find the area of triangle
# l=lambda a,b:1/2*a*b
# print(l(10,5))


#find largest of two number
# l=lambda a,b:a if(a>b) else b
# print(l(6,9))
#
#
# # using lambda find a number is odd or even
# x=lambda a:"even" if(a%2==0) else "odd"
# print(x(4))


# # find absolute value of the number using lambda if else
# x=lambda a:a*-1 if(a<0) else a
# print(x(7))


# #check a character passing into lambda is vowel or not
# x=lambda a:"Vowel" if(a=='a'or a=='e'or a=='i' or a=='o' or a=='u')  else "not vowel"
# print(x('d'))


# #convert the positive data into negative and neg to pos
# x=lambda a:a*-1
# print(x(-11))


#largest of three numbers?
# x=lambda a,b,c:a if(a>b and a>c) else(b if(b>c) else c)
# print(x(3,5,2))
# print(x(9,5,22))


#check a number passing into lambda function is positive or negative or zero
# x=lambda a:"Positive" if(a>0) else("Negative" if(a<0) else "zero")
# print(x(0))
# print(x(-33))
# print(x(22))


#write a program to find the smallest value of four number passing into the lambda
# x=lambda a,b,c,d:"%d is smallest"%a if(a<b and a<c and a<d) else("%d is smallest"%b if(b<c and b<d) else("%d is smallest"%c if(c<d) else "%d is smallest"%d))
# print(x(1,33,56,11))
# print(x(55,66,12,77))
# print(x(55,22,77,88))
# print(x(77,88,99,10))


