import numpy as np
arr = np.array([[1, 2,3,],[4,5,6]],dtype=complex)
print("The array is:\n",arr)
print("No.of Rows and columns:",arr.shape)
print("Dimension:",arr.ndim)
newarr=arr.reshape(3,2)
print("Reshape the array to 3 by 2 :\n",newarr)