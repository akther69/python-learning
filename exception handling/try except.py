#SYNTAX
# try:
     #code to be excecuted
# except:
#     code to be excecuted when error occur

#error are classified into two
#LOGIC ERROR
    #created by the programmer
    # eg syntax,indentation,name error etc
#RUNTIME ERROR
    #created by the end users
    #eg:zerodivision,filenotfound,valueeroor etc


#zerodivision error
# try:
#     a = int(input("enter a="))
#     b = int(input("enter b="))
#     c = a / b
#     print(c)
# except:
#     print("Number cannot divided by zero")


#valueerror
# try:
#     num=int(input("enter the number="))
#     print(num)
# except:
#     print("enter the number not character")


#zeroerror and valueerror
# try:
#     a = int(input("enter a="))
#     b = int(input("enter b="))
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("please input valid data")


#quadratic equation
import math
try:
    a = int(input("enter a="))
    b = int(input("enter b="))
    c = int(input("enter c="))
    d = (b ** 2) - (4 * a * c)
    print(d)
    if (d > 0):
        e = math.sqrt(d)
        f = (-b + e) / (2 * a)
        g = (-b - e) / (2 * a)
        print(f)
        print(g)
except ZeroDivisionError:
    print("cannot divisible by zero")
except ValueError:
    print("Enter the valid data")

