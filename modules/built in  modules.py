#math modules
import math
#it provides collection of math functions which is used to preform mathematical operation
# a=math.factorial(5)
# print(a)
#
#
# b=math.sin(1)
# print(b)
#
#
# c=math.sqrt(16)
# print(c)
#
#
# d=math.floor(10.6)
# print(d)
#
#
# e=math.ceil(10.4)
# print(e)


# help(math)


# def area(r):
#     a=math.pi*r**2
#     print(a)
# area(5)


#calendar modules
#it works with calendar classes and functions
import calendar

#to print month calendar
# year=int(input("Enter the year= "))
# month=int(input("Enter the month= "))
# a=calendar.month(year,month)
# print(a)


#to print entire calendar
# year=int(input("Enter the year= "))
# a=calendar.calendar(year)
# print(a)


#to check the leap year
# year=int(input("Enter the year= "))
# a=calendar.isleap(year)
# print(a)


#to start the week what we want
# year=int(input("Enter the year= "))
# a=calendar.TextCalendar(calendar.TUESDAY)
# print(a.formatyear(year))


#to start the day in tyhe month
# year=int(input("Enter the year= "))
# month=int(input("Enter the month= "))
# a=calendar.TextCalendar(calendar.TUESDAY)
# print(a.formatmonth(year,month))


#time module
#provide functions for working with time related datas
import time

# k=time.localtime()
# print(k)
#
# print("Year= ",k.tm_year)
# print("Year= ",k.tm_mon)
# print("Year= ",k.tm_mday)
# print("Year= ",k.tm_yday)
# print("Year= ",k.tm_hour)
# print("Year= ",k.tm_min)
# print("Year= ",k.tm_sec)


# to print the human  readable format time
# b=time.asctime()
# print(b)


# sleep()
# it is used add delay in the execution in the program
# print("hlooo")
# time.sleep(3)
# print("ooooooiii")


#strftime():string format time
# %A =day
# %B=month
# %d=date
# %D=complete date
# %Y=year
# %M=min
# %m=month
# %S=sec
# %H=hour
# a=time.strftime('%A')
# print(a)
# a=time.strftime('%B')
# print(a)
# a=time.strftime('%d')
# print(a)
# a=time.strftime('%D')
# print(a)
# a=time.strftime('%Y')
# print(a)
# a=time.strftime('%M')
# print(a)
# a=time.strftime('%m')
# print(a)
# a=time.strftime('%S')
# print(a)
# a=time.strftime('%H')
# print(a)
# a=time.strftime('%A %Y %B %d')
# print(a)


import datetime
#python datetime module supplies classes to work with date and time
#these classes provide a number of functions to deal with dates,times

# year=int(input("enter the year="))
# month=int(input("enter the month="))
# day=int(input("enter the day="))
# mydate=datetime.date(year,month,day)
# print(mydate)
# print(type(mydate))


# today=datetime.date.today()
# print(today)
# print("current year=",today.year)
# print("current month=",today.month)
# print("current day=",today.day)


#now()
# today=datetime.datetime.now()
# print("Current date and time=",today)


#timedelta()
#days after
# from datetime import timedelta
# d=datetime.date.today()
# d+=timedelta(days=100)
# print(d)

#days before
# from datetime import timedelta
# d=datetime.date.today()
# d-=timedelta(days=2)
# print(d)


#ramdom module
#python random module is an inbuilt module which is used to generate random numbers or datas
import random
# l=["akther","suhaib","shabs","vasu"]
# print(random.choice(l))


#randint()
#it is used to select random integers between the given range
#random.randint(start,end)
# lottery=random.randint(100,500)
# print(lottery)


#random.uniform():
#it is used to select random float number the given range
#random.uniform(start,end)

# r1=random.uniform(1,10)
# print(r1)


#shuffle():
#it is used to shuffle a list of element
# li=[1,2,3,4]
# random.shuffle(li)
# print(li)


#OS MODULE
#module in python that is used to interact with the operating system

import os

#getcwd() : to get the path of the current working directary
# cwd=os.getcwd()
# print("path of cwd=",cwd)


#mkdir:
#method used to create directory named path with specified numeric mode
#r==raw string used to remove special characters from the path
##f===formatting string
# os.mkdir(r"C:\Users\abdul\suhaib\pythonProject\olddir")
# print("Directory created")


# dir=input("Enter the directory name")
# os.mkdir((rf"C:\Users\abdul\suhaib\pythonProject\{dir}"))
# print("directory created")


#listdir()
# li=os.listdir(r"C:\Users\abdul\suhaib\pythonProject")
# print(li)


#rmdir()
#used to remove empty direction
# os.rmdir(r"C:\Users\abdul\suhaib\pythonProject\abiya")
# print("Removed Successfully")

#shutil.rmtree() it is used to remove the directory with file
# import shutil
# shutil.rmtree("path of directory")


#remove(): it is used to remove a file path(eg profile photo path)
# os.remove(r"")
# print("file deleted")
# nt=new technology

# print(os.name) #window nt is a microsoft window personal computer operating system




