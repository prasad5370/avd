import numpy as np
'''14. Accept 2 arrays from keyboard. Create a third array that contains the sum of corresponding elements of these two arrays.
 NOTE: Do not add the arrays as arr1+arr2.
 Read the elements from arr1 and arr2 using for loop, add them and then store them into the third array.
'''

a,b=[int(i) for i in input("how many rows and col :").split(',')]
#after creating arry store or fill the data with zeros only
arr1=np.zeros((a,b),dtype=int)
#know take the values from user and replce the zeros
print("enter arry elemnt row by row")

for i in range(a):
    arr1[i] =[int(i) for i in input().split()]
for i in range(a):

    print(arr1[i])

r,c=[int(i) for i in input("how many rows and col :").split(',')]
#after creating arry store or fill the data with zeros only
arr2=np.zeros((r,c),dtype=int)
#know take the values from user and replce the zeros
print("enter arry elemnt row by row")

for i in range(r):
    arr2[i] =[int(i) for i in input().split()]
for i in range(a):

    print(arr2[i])


arr3=[]
for i in range(a):
    arr3.append(arr1[i] + arr2[i])
print(arr3)

'''15. Accept a matrix from keyboard and sort its elements into descending order
on rows and columns separately. Display the sorted matrices.  '''

a,b=[int(i) for i in input("how many rows and col :").split(',')]
arr1=np.zeros((a,b),dtype=int)
print("enter arry elemnt row by row")
for i in range(a):
    arr1[i] =[int(i) for i in input().split()]
mat1=np.matrix(arr1)
print("sorted by rows :\n",np.sort(mat1,axis=1)[:, ::-1])

#slicing is used in revese part
print("sorted by colume : \n",np.sort(mat1,axis=0)[::-1, :])
