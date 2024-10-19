# regx rule to validate a string
# import re
# word=input("Enter the name=")
# rule="[A-Za-z]+"
# match=re.fullmatch(rule,word)
# if match:
#     print("Valid")
# else:
#     print("Invalid name")


#TASK
    #write a rule for validating a name only in the range 5,10
# import re
# word=input("Enter the Name=")
# rule="[A-Za-z]{5,10}"
# match=re.fullmatch(rule,word)
# if match:
#     print("Valid")
# else:
#     print("Invalid")


#TASK
#RULE
    #name should start with uppercase
    #followed by lowercase letter
    #total limit should be 5,10
# import re
# word=input("Enter the Name=")
# rule="[A-Z][a-z]{4,9}"
# match=re.fullmatch(rule,word)
# if match:
#     print("Valid")
# else:
#     print("Invalid")


#TASK
#RULE
    #name should only start with A,D,F
    #followed by lowercase total limit(5,10)
# import re
# word=input("Enter the Name=")
# rule="[ADF][a-z]{4,9}"
# match=re.fullmatch(rule,word)
# if match:
#     print("Valid")
# else:
#     print("Invalid")


#TASK
#RULE
    #name should only start with A,B,C
    #followed by the lowercase
    #number should be included or not included
# import re
# word=input("Enter the Name=")
# # rule="[ABC][0-9]*[a-z]+[0-9]*[a-z]*"
# rule="(([ABC][a-z0-9]+)|([ABC][a-z]))"
# match=re.fullmatch(rule,word)
# if match:
#     print("Valid")
# else:
#     print("Invalid")


#TASK
#RULE
    #user can input the number
    #valid the number if the range 10 else invalid
# import re
# word=input("Enter the Number=")
# rule="[0-9]{1,10}"
# match=re.fullmatch(rule,word)
# if match:
#     print("Valid")
# else:
#     print("Invalid")


#TASK
#RULE
    #phone number validation
    #only start with 9,8,7,6
    #total limit 10
# import re
# word=input("Enter the Name=")
# rule="[9876][0-9]{9}"
# match=re.fullmatch(rule,word)
# if match:
#     print("Valid phone number")
# else:
#     print("Invalid phone number")


#TASK
#RULE
    #it should only start with +91
    #followed by the phone number
    #total limit 10
import re
# word=input("Enter the Number=")
# rule="[+][9][1][6-9][0-9]{9}"
# match=re.fullmatch(rule,word)
# if match:
#     print("Valid phone number")
# else:
#     print("Invalid phone number")