#eg
# for i in range(100):
#     print("Hello Suhaib")
#question 1
# write a program to print yur name as per the limit input by the user
# n=int(input("Enter the limit = "))
# for i in range(n):
#     print("SUHAIB AKTHER S")
# #eg
# for i in range(10):
#     print(i)
#wrt a prm to print natural numbers in the limit input by the user
#n=int(input("Enter the limit = "))
# for i in range(n):
#     print(i+1)
#write a program to print 100 to 200 using loop
# for i in range(100,201):
#     print(i)
# enter the initial limit final limit
# initial=int(input("Enter the initial limit = "))
# final=int(input("Enter the final limit = "))
# for i in range(initial,final+1):
#     print(i)
#write a program to print a even number for in the range 1,21
# for i in range(1,21):
#     if(i%2==0):
#         print(i)
# write a program to print odd number in the range 100,500
# for i in range(100,500):
#     if(i%2!=0):
#         print(i)
#write a program to print first 10 even number
# for i in range(1,21):
#     if(i%2==0):
#         print(i)
#task
#write a program to print numbers divisible by 7 for in range 1,100
# for i in range(1,100):
#     if(i%7==0):
#         print(i)
#write a program to print numbers that are divisible by 2 but not by 11 in the range of 50,100
# for i in range(50,100):
#     if(i%2==0 and i%11!=0):
#             print(i)
#generate multiplication table of number input by the user
# n=int(input("Enter the number = "))
# for i in range(1,11):
#     print(n,"*",i ,"=",n*i)
#write a program the sum of first ten number natural number
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)
# write aprogram to find the product of first 6 natural number
# product=1
# for i in range(1,6):
#     product*=i
# print(product)
#write a program to count total number of even value fall in the range 100 to 150
# count=0
# for i in range(100,150):
#     if(i%2==0):
#         count+=1
# print(count)
# question
#write a program to find factorial of number input by the user
# factorial=int(input("Enter the number = "))
# fact=1
# for i in range(1,factorial+1):
#     fact*=i
# print("factoraial =",fact)
#write a program to find the sum of both even and odd number for in the range
# even=0
# odd=0
# for i in range(1,50):
#     if(i%2==0):
#         even+=i
#     else:
#         odd+=i
# print("The sum of even is =",even)
# print("The sum of odd is =",odd)
#generate fibonocci series
# 0 1 1 2 3 5 8
# fib=int(input("Enter the number = "))
# first=0
# second=1
# print(first)
# print(second)
# for i in range(fib-2):
#     third=first+second
#     print(third)
#     first=second
#     second=third
#for loop with three value
# for i in range(2,11,2):
#     print(i)
#question
# for i in range(100,501,100):
#     print(i)
#question
#write a program to print first ten natural number in reverse order
# for i in range(10,0,-1):
#     print(i)
#qusetion
# for i in range(5000,999,-1000):
#     print(i)
#question
# for i in range(-10,0,1):
#     print(i)

# number=int(input("Enter the number="))
# a=0
# b=1
# lst=""
# lst+=a
# lst+=b
# for i in range(number-2):
#     c=a+b
#     lst+=c
#     a=b
#     b=c
# print(lst)

# number = int(input("Enter the number of terms in the Fibonacci sequence: "))
# a, b = 0, 1
# fib_sequence = [a, b]
# for i in range(number - 2):
#     c = a + b
#     fib_sequence.append(c)
#     a, b = b, c
# output = " ".join(map(str, fib_sequence[:number]))
# print(output)


# find the square of numbers from the given list which is multiple of 5
# def square_of_number(num):
#     square_root=[]
#     for i in num:
#         if i%5==0:
#             l=i**2
#             square_root.append(l)
#     print(square_root)
#
# square_of_number([4,5,6,7,8,9,10])


# find the second largest number from the list
# def second_largest(num):
#     l=list(set(num))
#     k=sorted(l)
#     print(k[-2])
# second_largest([1,2,3,4,5])
# second_largest([6,7,8,9,9])
# second_largest([67,66,44,22,99])

# find the count of each character from the given list

# def count_of_each_number(num):
#     character=0
#     for i in num:
#         if str(i).isalpha():
#             character+=1
#     print(character)
# count_of_each_number([1,'a','b',1,2,3,'i'])



#find the median of the array
# def median_of_array(num):
#         remove_duplication=list(set(num))
#         sort=sorted(remove_duplication)
#         length=len(sort)
#         median=length//2
#         if length%2==1:
#             print(sort[median])
#         else:
#             print(sort[median-1]+(sort[median]-sort[median-1])/2)
# median_of_array([6,7,8,9])
# median_of_array([66,67,68,69])
# median_of_array([78,99,34,57])
# median_of_array([12,33,44,55,6,778,876,43345,6777,1234])
# median_of_array([11,22,55,66,777,888,999])

# def integer_to_roman(num):
#     val_roman=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
#                (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
#                (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),
#                (1,'I')]
#     roman_value=''
#     for value,roman in val_roman:
#         while num>=value:
#             roman_value+=roman
#             num-=value
#     print(roman_value)
# integer_to_roman(220)


# def char_count(char):
#     character={}
#     for i in char:
#         if i in character:
#             character[i]+=1
#         else:
#             character[i]=1
#             continue
#     print(character)
# char_count("suhaibbbb")


# def fibinnoci(num):
#     a,b=0,1
#     fib_ser=[0,1]
#     for i in range(num-2):
#         c=a+b
#         fib_ser.append(c)
#         a,b=b,c
#     print(" ".join(map(str,fib_ser[:num])))
# fibinnoci(5)


# def reveres(*string):
#      reversed=[]
#      fully_reveresed=[]
#      for i in string:
#          reverse=i[::-1]
#          reversed.append(reverse)
#      print(" ".join(reversed))
#      for i in reversed:
#          fullrev=fully_reveresed.append(i)
#          fully_reveresed.reverse()
#      print(fully_reveresed)
#
# reveres('blue',"green",'yellow')

