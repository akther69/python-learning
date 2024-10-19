# # # #write a program to count words in a string
# # # #input:hello world
# # # #output:2
# # # # def word(a):
# # # #     count=1
# # # #     for i in a:
# # # #         if(i==" "):
# # # #             count+=1
# # # #     return count
# # # # print(word("hello world welcome"))
# # # # print(word("hello world welcome to python"))
# # #
# # #
# # # #write a program to  find it is armstrong number
# # # # a=int(input())#153
# # # # x=len(str(a))
# # # # b=[]
# # # # for i in str(a):
# # # #     b+=i
# # # #     print(b)
# # # # for i in b:
# # # #     print(i)
# # #
# # #
# # #
# # #
# # # #check a number disarius or not
# # # # def num(a):
# # # #     temp=a
# # # #     w=len(str(a))
# # # #     for i in str(a):
# # # #         print(i)
# # # #     for j in range(1,w+1):
# # # #         print(j)
# # # # num(89)
# # # a=[1,2,3,4,5,1,2]
# # # b=[]
# # # for i in a:
# # #     if(i in b):
# # #         b.append(i)
# # #     else:
# # #         continue
# # # print(b)
# #
# #
# # # def armstrong(a,c):
# # #     b=[]
# # #     for num in range(a,c):
# # #         temp=num
# # #         length=len(str(a))
# # #         arm=0
# # #         while(num>0):
# # #             rem=num%10
# # #             arm+=rem**length
# # #             num//=10
# # #         if(arm==temp):
# # #             b.append(arm)
# # #     return b
# # # print(armstrong(1000,2000))


# def harshad(a):
#     sum=0
#     for i in str(a):
#         sum+=int(i)
#     if(a%sum==0):
#         return "%d is harshad"%a
#     else:
#         return "%d is not harshad"%a
# print(harshad(18))
# print(harshad(1234))

# #
# def disarius(num):
#     dis=0
#     temp=num
#     a=len(str(num))
#     while(num!=0):
#         rem=num%10
#         dis+=rem**a
#         num//=10
#         a-=1
#     if(temp==dis):
#         return "disarium"
#     else:
#         return "not disarium"
# print(disarius(89))


# # def lst(a):
# #     u=[]
# #     for i in a:
# #         if(i in a):
# #
# #         else:
# #
# # def is_palindrome(teststr):
# #     copy=teststr.lower()
# #     x=''
# #     for i in teststr:
# #         x=i+x
# #     x=x.lower()
# #     print(x)
# #     if(x==copy):
# #         return True
# #     else:
# #         return False
# # print(is_palindrome("malayalam"))
# # print(is_palindrome("Radar"))
#
# # n = int(input())
# # arr = list(map(int, input().split()))
# # ordered=list(set(arr))
# # d=sorted(ordered)
# # print(d[-2])
#
# # import pymysql
# # db=pymysql.connect(host="localhost",user="root",password="")
# # mycursor=db.cursor()
# # sql="create database hindusthan_management"
# # mycursor.execute(sql)
# # db.commit()
#
# # import pymysql
# # db=pymysql.connect(host="localhost",user="root",password="",database="hindusthan_management")
# # mycursor=db.cursor()
# # sql="create table hindusthan_details(id int auto_increment,college varchar(100),department varchar(100),builting varchar(100),primary key(id))"
# # mycursor.execute(sql)
# # db.commit()
# # print("table created successfully")
#
# # import pymysql
# # db=pymysql.connect(host="localhost",user="root",password="",database="hindusthan_management")
# # mycursor=db.cursor()
# # sql="insert into hindusthan_details(college,department,builting) value('autonomys','CHEM','G Block')"
# # mycursor.execute(sql)
# # db.commit()
# # print("table insertion successfully")
#
# # import pymysql
# # db=pymysql.connect(host="localhost",user="root",password="",database="hindusthan_management")
# # mycursor=db.cursor()
# # sql="update  hindusthan_details set department='Food' where id=1"
# # mycursor.execute(sql)
# # db.commit()
# # print("table updation successfully")
#
#
# # import pymysql
# # db=pymysql.connect(host="localhost",user="root",password="",database="hindusthan_management")
# # mycursor=db.cursor()
# # sql="delete from  hindusthan_details where id=1"
# # mycursor.execute(sql)
# # db.commit()
# # print("table deletion successfully")
#
# x = int(input())
# #1
# y = int(input())
# #1
# z = int(input())
# #2
# n = int(input())
# #3
# coordinates = [
#     [i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)
#     if i + j + k != n
# ]
#
# print(coordinates)
#
#
# cor=[[i,j,k] for i in range]
# num=5
# a=1
# for i in range(1,num+1):
#     a*=i
# print(a)
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# coordinates = [
#     [i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)
#     if i + j + k != n
# ]
#
# print(coordinates)

#combinations
# import itertools
#
# # Read inputs
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# z = int(input("Enter z: "))
#
# # Create a list of the inputs
# inputs = [x, y, z]
#
# # Initialize an empty list to store all combinations
# combinations = []
#
# # Generate combinations of all lengths from 1 to len(inputs)
# for r in range(1, len(inputs) + 1):
#     combinations.extend(itertools.combinations(inputs, r))
#
# # Convert the combinations to a set to ensure uniqueness and then to a list for printing
# unique_combinations = [list(comb) for comb in set(combinations)]
#
# # Print all unique combinations
# for combination in unique_combinations:
#     print(combination)

# array
# n = int(input())
# arr = list(map(int,input().split()[:n]))
# print(arr)

# n = int(input())
# arr = list(map(int, input().split()[:n]))
# d=sorted(arr)
# print(d[-2])

# n = int(input())
# for i in range(n):
#     names = input()
#     mark = float(input())


# n=int(input())
# students=[]
# for i in range(n):
#     name=input()
#     mark=float(input())
#     students.append([name,mark])
# grades=sorted(set(mark for name,mark in students))
# second_lowest_grade=grades[1] if len(grades)>1 else None
# stu_second_lowest_grade=[name for name,mark in students if mark==second_lowest_grade]
# for students in stu_second_lowest_grade:
#     print(students)

# Read the number of students
# n = int(input().strip())

# # Initialize an empty dictionary to hold student marks
# student_marks = {}
#
# # Read student names and their marks
# for _ in range(n):
#     data = input().strip().split()
#     name = data[0]
#     marks = list(map(int, data[1:]))
#     student_marks[name] = marks
#
# # Read the student name for which to calculate the average
# query_name = input().strip()
#
# # Calculate and print the average marks for the specified student
# if query_name in student_marks:
#     marks = student_marks[query_name]
#     average = sum(marks) / len(marks)
#     print(f"{average:.2f}")
# else:
#     print(f"Student {query_name} not found.")

# n=int(input())
# value=list(map(int,input().split()[:n]))
# tup=tuple(value)
# print(hash(tup))

# n=input()
# result=n.swapcase()
# print(result)

# n=5
# for i in range(n):
#     for k in range(i):
#         print(' ',end="")
#     for j in range(n,i,-1):
#         print("*",end=" ")
#     print()

# n=3
# for i in range(n):
#     for k in range(2-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# n=3
# for i in range(n+1):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(3-i):
#         print("*",end=" ")
#     print()
#
# n=3
#
# for i in range(n):
#     for k in range((n-1)-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(1,n):
#     for k in range(i):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(n-i,end=" ")
#     print()

# n=3
# for i in range(n):
#     for j in range(n-i):
#         print(chr(100-(i+1)),end=" ")
#     print()

# num=0
# for i in range(1,5):
#     for j in range(i):
#         num+=1
#         print(num,end=" ")
#     print()

# n=3
# for i in range(n):
#     for k in range((n-1)-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()

# for i in range(1,5):
#     for k in range(4-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print(i,end=" ")
#     print()
# for i in range(1,4):
#     for k in range(i):
#         print(" ",end=" ")
#     for j in range(4-i):
#         print(4-i,end=" ")
#     print()

# for i in range(1,6):
#     for k in range(9-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(1,6):
#     for k in range(7-i):
#         print(" ",end="")
#     for j in range(i+2):
#         print("*",end=" ")
#     print()
# for i in range(1,6):
#     for k in range(5-i):
#         print(" ",end="")
#     for j in range(i+4):
#         print("*",end=" ")
#     print()
# for i in range(1,3):
#     for k in range(3):
#         print(" ",end=" ")
#     for j in range(2):
#         print("*",end=" ")
#     print()


# s="1 w 2 r 3g"
# data=s.title()
# print(data)

# def print_rangoli(size):
#     import string
#     alphabet = string.ascii_lowercase
#
#     # Calculate the width of the rangoli
#     width = 4 * size - 3
#
#     # Generate the pattern for the top half
#     pattern = []
#     for i in range(size):
#         left_part = alphabet[size-1:i:-1]
#         right_part = alphabet[i:size]
#         s = '-'.join(left_part + right_part)
#         pattern.append(s.center(width, '-'))
#
#     # Combine the top and bottom halves and print the rangoli
#     full_pattern = pattern[::-1] + pattern[1::]
#     print('\n'.join(full_pattern))

# import textwrap
# def merge_the_tools(string, k):
#     lst=[]
#     # your code goes here
#     code=textwrap.fill(string,k)
#     print(code)
# merge_the_tools("AABCAAADA",3)

# x=1
# d=x<<2
# print(d)

# n=int(input("enter the number"))
# for i in range(1,11):
#     print(i,"*",n,"=",i*n)

# n=int(input("enter the number="))
# factorial=1
# for i in range(1,n+1):
#
#     factorial*=i
#
# print(factorial)

# fib=int(input("enter the number="))
#
# fst=0
#
# print(fst)
#
# snd=1
#
# print(snd)
#
# for i in range(fib-2):
#
#     thd=fst+snd
#
#     print(thd)
#
#     fst=snd
#
#     snd=thd

# n=int(input("ent num="))
#
# lnt=len(str(n))
#
# arm=0
#
# copy=n
#
# while(n!=0):
#
#     mod=n%10
#
#     arm=mod**lnt+arm
#
#     n//=10
#
# if(copy==arm):
#
#     print("armstrong number")
#
# else:
#
#     print(" not armstrong")

# c c c
# b b
# a
# for i in range(100,96,-1):
#     for j in range(96,i):
#         print(chr(i),end=" ")
#     print()

# n=6
# for i in range(n,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()


# n=4
# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n=3
# for i in range(n):
#     for k in range((n-1)-i):
#          print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for k in range((n-i)):
#          print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

