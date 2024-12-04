'''5. Accept a character from the keyboard. Write a program to check if a given character is a vowel or consonant.
Note: Vowels are a,e,i,o,u.'''

'''#create a variable then store the str in it
char=str(input("enter the single charater from a-z :"))
#use inoprator to check the charter 
if char in 'aeiou':
    print('its vowel')
else: 
    print("its consonant")'''



'''6. Write a program to check if a given number is prime or not.
Note: Prime number is a number that is not divisible by any other number except by 2 and itself.'''

#take a input from user 
x=int(input("enter a positive integer no: "))
#prime no should be positive and greter then 1
if x<=1:
    print("this is not prime no")
#2 is only even prime no so sepret condition for it
elif x==2:
    print("this is the prime no")
#in range x+1 is becuse range will go for second last term only
else:
    for i in range(2,x+1):
      if x % i== 0:
         print("this is not prime no")
         break
      else:
        print("this is a prime no")
        break

#i used break more time becouse its showing repitation of print stmt'''
 
'''7. Write a program to generate prime number series.
Note: you have to display n primes as: 2,3,5,7,11,13,17,19, etc.'''


x=int(input("enter the highest no to print prime no upto :"))
for num in range(2,x+1):
    prime_flag = True
    for i in range(2,num):
        if (num%i==0):
            prime_flag = False
    if prime_flag:
       print (num)


'''8. 1. Write a Python program to reverse a list of numbers given.
Ex: the given list is [10, 20, 5, 4, 33, 22]
Your program should print [22, 33, 4, 5, 20, 10]
Note: Do the above program without using slicing and reverse() methods. '''

'''a=[10, 20, 5, 4, 33, 22]
rev=[]
for i in a:
    rev.insert(0,i)
print(rev)'''

lst=[]
lst=(input("enter the values:"))
print(lst)