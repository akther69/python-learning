#REGULAR EXPRESSION(REGX)
#it is defined as a sequence of character which are used to search for a pattern in string
#RE is used for regular expression(regx) in python

#SOME BUILT IN FUNCTION USED IN REGULAR EXPRESSION

#fullmatch():
    #it returns true if match is found

#search():
    #it return match object

#findall():
    #it return the list that contains all match

#split():
    #it returns a string has been split

#sub():
    #it is use to replace the matches


#a regular expression is created using mix of characters special sequence and sets


#CHARACTERS
#[] : it represents a set of characters

#\ : it represents special sequence \s,|d,|w

#^ : it represents pattern present at the begining of a string

#* : it represents 0 or more occurance

#+ : it represents 1 or more occurance

#{} : specified number of occurance of pattern

#| : it represents this or that character is parent


#RULES OF REGULAR EXPRESSION:

#x='[abc]' : either a,b or c

#x='[^abc]' : except abc

#x='[a-z]' : lowercase a to z

#x='[A-Z]' : uppercase A to Z

#x='[a-zA_Z]' : both lower and uppercase

#x='[0-9]' : it checks the digit

#x='[a-zA-Z0-9]' : lower,upper or digit


#SPECIAL SEQUENCE:

#x='\s' : check space

#x='\d' : check digit

#x='\D' : it returns string except number

#x='\w' : it returns a string contains word


#QUANTIFIERS

#x='[a-z]+' : 1 or more

#x='[a-z]*' : 0 or more

#x='[a]?' : a include or not include

#x='[a]{n}' : n=number [a-z]{2}

#x='[a]{n,k}' : n=minimum number k=maximum number