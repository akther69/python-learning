try:
    num=int(input("Enter a number="))
    if num>=1 and num<=10:
        print("success")
    else:
        raise Exception
except Exception:
    print("please input a number between 1 and 10")


#question
#take a name input from the user,if the name contains only alphabets print"welcome"{{name}}
#else it should raise an error"plz input a valid name"
# try:
#     name=input("Enter the name=")
#     if(name.isalpha()):
#         print("Welcome",name)
#     else:
#         raise Exception
# except Exception:
#     print("plz input a valid name")