'''9. Write a function that accepts monthly salary of employee and calculates annual salary (for 12 months).
 This annual salary should be returned to another function that calculates provident fund at 12.5% of annual salary.'''

def montly_sal(x):
    return x*12

def Cal_pf(z):
    return z*0.125

l=Cal_pf(montly_sal(1000))
print("total pf according to annual sal",l)

#another way 

def month_sal(x):
    return x*12

def pf(montH_sal):
    c=month_sal(1000)*0.125
    return c
    
g=pf(month_sal)
print(g)
#10. Write a function to calculate factorial value of a given number without using recursion.

x=int(input("enter the positive no to find facto: "))
def fact(x):
    y=1
    for i in range(1,x+1):
        y=y*i
    return y
z=fact(x)
print (z)

#11. Write a function that accepts a string and returns the number of chars in the string. 
y=str(input("enter the string  :" ))
def cal_char(y):
    print("count of char:",len(y))

cal_char(y)

#another way

y=str(input("enter the string  :" ))

def cal_char(y):
    count=0
    for i in range(0,len(y),1):
        count=count+1
    print(count)    

cal_char(y)
