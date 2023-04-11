# Approach 1: Temporary variable
print("Approach 1")
mylist = [12, 35, 9, 56, 24]  # index starts from 0
size = len(mylist)
temp = mylist[0]
mylist[0] = mylist[size - 1]
mylist[size - 1] = temp
print('List after swapping', mylist)

# Approach 2: swapping
print("Approach 2")
mylist = [12, 35, 9, 56, 24]  # index starts from 0
mylist[0], mylist[-1] = mylist[-1], mylist[0]
print('List after swapping', mylist)

# Approach 3: using tuple
print("Approach 3")
mylist = [12, 35, 9, 56, 24]  # index starts from 0
get = (mylist[-1], mylist[0])  # Packing 24 12
mylist[0], mylist[-1] = get
print('List after swapping', mylist)

# Approach 4: * operand
print("Approach 4")
mylist = [12, 35, 9, 56, 24]  # index starts from 0
start, *middle, end = mylist
print(start)
print(middle)
print(end)
mylist = [end, *middle, start]
print('List after swapping', mylist)

# Approach 5: using pop()
print("Approach 5")
mylist = [12, 35, 9, 56, 24]  # index starts from 0
first = mylist.pop(0)
last = mylist.pop(-1)
mylist.insert(0, last)
mylist.append(first)
print('List after swapping', mylist)
