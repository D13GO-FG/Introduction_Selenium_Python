# Approach : using loop
mylist = [1, 6, 3, 5, 3, 4]
ele = 8
flag = 0

for i in mylist:
    if i == ele:
        print("Element found")
        flag = 1
        break

if flag == 0:
    print("Element not found")

# Approach : using in operator
mylist = [1, 6, 3, 5, 3, 4]
ele = 8
if ele in mylist:
    print("Element found")
else:
    print("Element not found")
