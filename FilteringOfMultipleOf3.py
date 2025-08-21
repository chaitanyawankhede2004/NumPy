import numpy as np

arr = np.DynamicArray([])
print("Printing Original Array :", arr)

for i in range(5):
	L=int(input())
	arr.insert(L)
filtering=[]
for i in range(len(arr)):
	if arr[i]%3==0:
		filtering.append(True)
	else:
		filtering.append(False)
print("Filtering Array ",filtering)

newarr = arr[filtering]
print("Filtered Array :", newarr)

