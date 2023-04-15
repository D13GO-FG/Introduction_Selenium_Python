# Approach 1: using slicing technique
print("Approach 1: using slicing technique")
mylist = [4, 8, 2, 10, 15, 18]
mylist_copy = mylist[:]
print(mylist_copy)

# Approach 2: using extend() method
print("Approach 2: using extend() method")
mylist = [4, 8, 2, 10, 15, 18]
mylist_copy = []
mylist_copy.extend(mylist)
print(mylist_copy)

# Approach 3: using the list() method
print("Approach 3: using the list() method")
mylist = [4, 8, 2, 10, 15, 18]
mylist_copy = list(mylist)
print(mylist_copy)

# Approach 4: using the copy() method
print("Approach 4: using the copy() method")
mylist = [4, 8, 2, 10, 15, 18]
mylist_copy = mylist.copy()
print(mylist_copy)

# Approach 5: using list comprehension
print("Approach 5: using list comprehension")
mylist = [4, 8, 2, 10, 15, 18]
mylist_copy = [i for i in mylist]
print(mylist_copy)
