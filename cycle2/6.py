import numpy as np
x = np.array([[2, 4, 6,1], [6, 8, 10,1],[1, 2, 1,1], [1, 1, 1,1]])
print(x,"\n")
print("Display all elements excluding the first row\n")
print(x[1:])
print("\nDisplay all elements excluding the last column\n")
print(x[:, :3])
print("\nDisplay the elements of 2 nd and 3 rd column\n")
print(x[:, 1:3])
print("\nDisplay 2 nd and 3 rd element of 1 st row\n")
print(x[0,1])
print(x[0,2])
a = np.array([1,2,8,9,3,4,5,6,7])
print(a)
array_copy = np.sort(a)[::-1]
print(array_copy[4:10])
