#filter()
#filter() that takes the sequence of arguments this will filter out the all the elements in the sequence
#filter() doesn't need looping
#syntax
#   x=list(filter(lambda argument:expresion,li))
#write a program to filter out even numbers from the given list
# li=[1,2,3,4,5,6]
# x=list(filter(lambda i:i%2==0,li))
# print(x)


#1.['a','b',3,2] filter out the alphabet from the list
# li=['a','b',3,2]
# x=list(filter(lambda i:str(i).isalpha(),li))
# print(x)
#
#
# # ['a','b','e','f'] filter out the vowels
# li=['a','b','e','f']
# x=list(filter(lambda i:i in "aeiouAEIOU",li))
# print(x)
#
#
# # [1,2,3,4,5,6,7] filter out which divisible by 2 not 3
# li=[1,2,3,4,5,6,7,8]
# x=list(filter(lambda i:(i%2==0 and i%3!=0),li))
# print(x)