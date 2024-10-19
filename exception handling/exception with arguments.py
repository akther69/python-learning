#exception with arguments
#in exception block arguments are used to gain aditional information about the error encountered
# try:
#     //body
# except ZeroDivisionError  as argument_name:
#     print(argument_name)

# try:
#     a=int(input("enter num1="))
#     b=int(input("enter num2="))
#     c=a/b
#     print(c)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as v:
#     print(v)


#what is finally block in exception handling?
# try:
#     a=int(input("enter num1="))
#     b=int(input("enter num2="))
#     c=a/b
#     print(c)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as v:
#     print(v)
# finally:
#     print("Execution ended")

#what is else block in exception handling?