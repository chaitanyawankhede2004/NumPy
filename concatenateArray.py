n = int(input("Enter number of rows in first array: "))
m = int(input("Enter number of rows in second array: "))
p = int(input("Enter number of columns for both arrays: "))

print("Enter",n,"rows for first array:")
array_1 = eval(input("eg ; [1, 2,3.. ]"))

print("Enter",m,"rows for second array:")
array_2 = eval(input("eg ; [1, 2,3.. ]"))

result = array_1 + array_2

print("Concatenated array:")
for row in result:
    print(row)
