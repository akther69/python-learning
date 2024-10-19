#unordered collection of data
#unindex position
#duplication not allowed

s={"a",'b','c','d',1,2,3}
# print(s)
# print(type(s))

#set() to convert to set  use this constructor

#add
# s.add("k")
# print(s)


#question using set method remove duplication of given list
# li=['a','b','a','b','c','c','d']
# k=list(set(li))
# k.sort()
# print(k)

#qst writea program to create a set of data input by the user
# num=int(input('Enter the number of element: '))
# st=set()
# for i in range(num):
#     setvalue=input("Enter the set values: ")
#     st.add(setvalue)
# print(st)


#pop()
# li={'a','b','a','b','c','c','d'}
# li.pop()
# print(li)


# used to remove the element with the name
# li={'a','b','a','b','c','c','d'}
# li.remove("d")
# print(li)


#discard()same as remove if the element not present in the set it doesn't an error but remove() will raisde an error if the element is not found
# li={'a','b','a','b','c','c','d'}
# li.discard("x")
# print(li)


#updatde()
# li.update('x','y','z')
# print(li)
# #
# li.update(['x','y','z',1,2,3])
# print(li)
#
# li.update(('x','y','z',1,2,3))
# print(li)

#intersection_update it is used to take common element in the set
# x={'a','b','c'}
# y={'a','d','e'}
# x.intersection_update(y)
# print(x)


#symmetric_difference_update()
# x={'a','b','c'}
# y={'a','d','e'}
# x.symmetric_difference_update(y)
# print(x)


#union()
# a={'a','b','c',1,2,3,4,5,7}
# b={'a','b','e','f'}
# c=a.union(b)
# print(c)

