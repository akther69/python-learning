#3.	Write a program to find the count of numbers which are the multiple of 5 fall between the initial range and final range  input by the user ?
# a=int(input("Enter the initial range = "))
# b=int(input("Enter the final range = "))
# count=0
# for i in range(a,b):
#     if(i%5==0):
#         count+=1
# print(count)
#4.	Write a program to find the product of numbers which divisible by 5 and not by 10
#Fall in the range 1 to 100 ?
# product=1
# for i in range(1,100):
#     if(i%5==0 and i%10!=0):
#         product*=i
# print(product)

#5.	Nested if
# If Male and age in the range  18 and 30 ,print Queue 1
# If female and age in the range 18 and 30 , print Queue 2
# If male   and age in the range 31 and 50 , print Queue 3
# If female and age in the range 31 and 50, print Queue 4
# And any other input of age should print Out Of Queue
# age=int(input("Enter the age = "))
# gender=input("Enter the gender = ").lower()
# if(age>=18 and age<=30):
#     if(gender=="male"):
#         print("Queue 1")
#     elif(gender=="female"):
#         print("Queue 2")
# elif(age>=31 and age<=50):
#     if(gender=="male"):
#         print("Queue 3")
#     elif(gender=="female"):
#         print("Queue 4")
# else:
#     print("Out Of Queue")
#question 6
# maths_mark=int(input("Enter the maths score = "))
# science_mark=int(input("Enter the science score = "))
# if(maths_mark>=60 and science_mark>=60):
#     print("Congratulations! You have passed both subjects.")
# elif(maths_mark>=60 and science_mark<60):
#     print("you need to improve your science score.")
# elif(maths_mark<60 and science_mark>=60):
#     print("you need to improve your math score.")


#question 7
for i in range(1,11):
    print(i,":",i**2)















