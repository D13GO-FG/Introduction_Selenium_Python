# Input : [5, 10, 15, 20]
# Output : 50

# Method 1: using for loop with range()
mylist = [5, 10, 15, 20]
total = 0

for i in range(len(mylist)):
    total = total + mylist[i]
print("Sum of all elements in given list: ", total)

# Method 2: using sum() method
mylist = [5, 10, 15, 20]
total = sum(mylist)
print("Sum of all elements in given list: ", total)