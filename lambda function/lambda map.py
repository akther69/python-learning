# map()
# it is an inbuilt function that allow to process and transform the data in an iterable without using the for loop
# the expression used in the map is applied to every elements
#syntax
#   x=list(map(lambda argument:expression,li))


#find the square of the each element of given list using map
# li=[1,2,3,4]
# x=list(map(lambda i:i**2,li))
# print(x)


#find the reverse of each string in the given list using lambda
# str=["hello","hai","welcome"]
# x=list(map(lambda i:i[::-1],str))
# print(x)


#mapping two list
# li1=[1,2,3,4]
# li2=[4,5,6,5]
# x=list(map(lambda i,j:i+j,li1,li2))
# print(x)