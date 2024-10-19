word="hello world"
# #len()
# print(len(word))


# #upper()
# print(word.upper())


# #lower()
# print(word.lower())


# #tittle
# print(word.title())


# #capitalize()
# print(word.capitalize())


# #swap()
# print(word.swapcase())


# #find()
# print(word.find('h'))
# #it returns -1 if the element is not found


# #index
# print(word.index('l'))


# #strip()
# print(word.strip())
# name=input("Enter the name = ").strip()
# if(name=='hai'):
#     print("Welcome")
# rstrip()=remove space in right side
# lstrip()=remove space in left side


# #split()
# print(word.split())
#split() always return list


# #replace()
# print(word.replace("world","welcome"))


# #string checking methods
# # isalpha()
# # isalnum()
# # isdigit()
# # istitle()
# # isupper()
# # islower()


# for i in range(0,5):
#     word=input("Enter the string = ")
#     print(word.isalnum())
#     print(word.isalpha())
#     print(word.istitle())
#     print(word.isdigit())
#     print(word.isupper())
#     print(word.islower())


#string iteration
# str="hello"
# for i in str:
#     print(i)


#write a program to find the length of the string input by the user with out using len function
# a=input("Enter the string = ")
# count=0
# for i in a:
#     count+=1
# print(count)


#write a program to remove the space without using the inbuit function
# a=input("enter the string = ")
# for i in a:
#     if(i!=" "):
#         print(i,end="")


# for i in a:
#     if(i==" "):
#         continue
#     else:
#         print(i,end="")


# b=''
# for i in a:
#     if(i!=" "):
#         b+=i
# print(b)


#write a program to reverese the string input by the user
# b=''
# for i in a:
#     b=i+b
# print(b)


#write a program to check if it is palindrome
# word=input("Enter the word = ")
# # q=word
# b=""
# for i in word:
#     b=i+b
# if(b==word):
#     print("it is palindrome")
# else:
#     print("it is not palindrome")


#string slicing
# it is method of accessing the part of sequence
#slicing is done using index postion
# word="suhaib akther"
# print(word[0:3])
# print(word[0:])
# print(word[:])
# print(word[:11])
# print(word[::-1])


# reverse a string using index position
# a=input("Enter the string = ")
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev+=a[i]
# print(rev)

# a=input("Enter the string = ")
# b=""
# for i in a:
#     if(i not in b):
#         b+=i
# print(b)


#write a program to input the string to display only character with even index value
# a=input("Enter the string = ")
# for i in range(0,len(a),2):
#         print(a[i],end="")
# print(a[::2])
