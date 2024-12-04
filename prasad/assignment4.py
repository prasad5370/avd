from functools import*
#12. Create a lambda that returns only negative numbers from a tuple.

lst=(1,2,3-4,-5,-6)

a=filter(lambda x:x<0,lst)
print(a)
for i in a:
    print(i)
#13. Create a lambda to calculate cumulative sum of all elements in a list.
lstt=[10,20,30,40]
b=reduce(lambda x,y:x+y,lstt)

print("sum of the number:" ,b)