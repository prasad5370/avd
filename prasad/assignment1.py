"""1. Write a Python program to reverse a list of numbers given.
Ex: the given list is [10, 20, 5, 4, 33, 22]
Your program should print [22, 33, 4, 5, 20, 10]"""

#store this list in a varible
lst=[10, 20, 5, 4, 33, 22]
#use string slicing 
print(lst[ : :-1])

"""2. Write a program to find out how many strings are there in the given list.
Ex: the given list is [10, 20, 'aaa', 'bbb', 33.5, 'ccc', 88, 'bbb', 25]
Your program output: There are 4 strings in the given list."""


#store the list in variable
lst=[10,20,'aaa','bbb',33.5,'ccc',88,'bbb',25]
#declear variable count and set to zero
count=0
#use for loop for list, type() this function is used to see the datatype of variable
for i in lst:
    if type(i)==str:
        count=count+1

#print the count variable
print("there are ",count,"string in the given list ")



"""3. Write a program to count the number of zeros in a given number.
Ex: the given number is 10203
Your program output: There are 2 zeros in the given number."""

#store the number in any variable
a=10203
#then conver datatype of a to str datatype and store in another variable
b=str(a)

#now we can apply string functions or methods to this,here we use count() method 
print("there are ", b.count('0'), "zerosin the given number")

"""4. Write a program to know if a given string is palindrome or not. Note: Palindrome is a string that gives the same string when reversed.
Ex: the given string is 'malayalam'
Your program output: malayalam is palindrome."""


#create variable then store the string 
plword="malayalam"

#use codition stment and slicing to revers the string

if plword==plword[::-1]:
    print( plword,"this is palidrom")
else: print(plword,"this not palidrom")

