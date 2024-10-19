#in python user can define custom exception by creating a new class
#this exception class has to be derived either directly or indirectly from the built in exception class
# class negavtive_error(Exception):
#     pass
# class zero_error(Exception):
#     pass
# try:
#     num=int(input("Enter the number="))
#     if num==0:
#         raise zero_error
#     elif num<0:
#         raise negavtive_error
#     else:
#         print("success")
# except negavtive_error:
#     print("negative error raised")
# except zero_error:
#     print("zero error raised")


#question
class tooOldexception(Exception):
    pass
class tooyoungexception(Exception):
    pass
try:
    age=int(input("Enter the age:"))
    if age<=20:
        raise tooyoungexception
    elif age>=51:
        raise tooOldexception
    else:
        print("successfully registered")
except tooOldexception:
    print("Very old to register")
except tooyoungexception:
    print("very young to register")