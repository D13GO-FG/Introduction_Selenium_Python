# Method 1
myList = [10, 20, 4, 45, 99]
myList.sort()
print(myList)       # [4, 10, 20, 45, 99]

print("First largest number is: ", myList[-1])
print("Second largest number is: ", myList[-2])

# Method 2
myList = [10, 20, 4, 45, 99]
new_list = set(myList)
print(new_list)
new_list.remove(max(new_list))
print(new_list)  # {4, 10, 45, 20}
print("Second largest number is: ", max(new_list))


