import numpy as np
arr = np.array([1, 2, 3, 4, 5,6,7,8,7,9,10])

#printing using elemnt
print(arr)
for i in arr:
	print(i,end=" ")
print()

#printing using index 	
for i in range(len(arr)):
	print(arr[i],end=" ")
print()
#sliceing
print("Elemnts from index 0 -4 :" , arr[0:5])
print("Elemnts in reverse :" , arr[::-1])
print("Elemnts from end 4th :" , arr[-4:])
print("Elemnts from index 2-6:" , arr[2:7])

print('2D Array : ') 
ArR = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(ArR)

print('3D Array : ')
rr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np.nditer(rr):
  print(x)
 

huj = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(huj):
  print(x)


x = np.where(arr == 4)

print(x) 
