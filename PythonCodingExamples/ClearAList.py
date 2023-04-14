# Approach 1: using clear() method

mylist = [6, 0, 4, 1]
print("mylist before clear: ", mylist)
mylist.clear()
print("mylist after clear: ", mylist)

# Approach 2: initializes the list with no value
mylist = [6, 0, 4, 1]
print("mylist before clear: ", mylist)
mylist = []
print("mylist after clear: ", mylist)

# Approach 3: using "*=0" this method removes all elements of the list and makes it empty
mylist = [6, 0, 4, 1]
print("mylist before clear: ", mylist)
mylist *= 0  # delete list
print("mylist after clear: ", mylist)

# Approach 4: using del
mylist = [6, 0, 4, 1]
print("mylist before clear: ", mylist)
# del mylist[1:3]     # 0 4
del mylist[:]   # delete all the elements
print("mylist after clear: ", mylist)
