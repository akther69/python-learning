#task
#write a program to print first ten natural number using while
# i=1
# while(i<=10):
#     print(i)
#     i+=1
#write a program to print first 10 even number using while
# i=2
# while(i<=20):
#     print(i)
#     i+=2


# i=1
# while(i<=20):
#     if(i%3!=0):
#         print(i)
#     i+=1


#write of program to find sum of digit of the number input by the user
# a=int(input("enter the number = "))
# sum=0
# while(a!=0):
#     rem=a%10
#     sum+=rem
#     a//=10
# print(sum)


#write a program to find the product of digit of the number
# a=int(input("Enter the number = "))
# product=1
# while(a!=0):
#     mod=a%10
#     product*=mod
#     a//=10
# print(product)


#write a program to find the reverse of the number input by the user
# a=int(input("Enter the number = "))
# rev=0
# while(a!=0):
#     mod=a%10
#     rev=rev*10+mod
#     a//=10
# print(rev)


#write a program to check a number by the user is palindrome number
# a=int(input("Enter the number = "))
# rev=0
# copy=a
# while(a!=0):
#     mod=a%10
#     rev=rev*10+mod
#     a//=10
# if(copy==rev):
#     print("The given number is palindrome number")
# else:
#     print("The given number is not palindrome number")


#write a program to check the number is armstrong or not
a=int(input("Enter the number = "))
length=len(str(a))
copy=a
arm=0
while(a!=0):
    mod=a%10
    arm=mod**length+arm
    a//=10
# print(arm)
if(copy==arm):
    print(copy,"is a armstrong number")
else:
    print(copy,"is not a armstrong number")

