import numpy as np

ar=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print("Original Array :\n",ar)

arr1=ar.reshape(4,3)
print("Reshaped array of  2-D Array of (4*3) :\n",arr1)

arr2=ar.reshape(3,2,2)
print("Reshaped array of  3-D Array of (3*2*2) :\n",arr2)

