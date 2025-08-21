import numpy as np

arr = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
print("Printing Original Array :", arr)

x = np.array([True, False, True, False, True, False, True, True, False])
print("Filtering Array :", x)

newarr = arr[x]
print("Filtered Array :", newarr)
