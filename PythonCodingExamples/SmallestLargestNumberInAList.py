# Input : myList = [20, 100, 20, 1, 10]
# Output :
# Smallest is 1
# Largest is 100

# Method 1: Sort the list in ascending order and print the first & last elements in the list
myList = [20, 100, 20, 1, 10]
myList.sort()  # sorting
print(myList)   # [1, 10, 20, 20, 100]

print("Smallest element is: ", myList[0])   # 1
print("Largest element is: ", myList[-1])   # 100

# Method 2: using min() & max() methods
myList = [20, 100, 20, 1, 10]
print("Smallest element is: ", min(myList))
print("Largest element is: ", max(myList))
