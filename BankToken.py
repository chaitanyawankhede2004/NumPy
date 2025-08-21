import numpy as np

arr = np.array([1010,1021,1234,1436,1119,1999,1013])
print("Printing Original Array :", arr)

oddF=[]
evenF=[]
for i in range(len(arr)):
	if arr[i]%2==0:
		evenF.append(True)
		oddF.append(False)
	else:
		oddF.append(True)
		evenF.append(False)


print("Even Token Numbers : ",arr[evenF])

print("Odd Token Numbers :",arr[oddF])
