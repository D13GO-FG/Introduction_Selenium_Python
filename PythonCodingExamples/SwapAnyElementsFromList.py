# Approach 1 simple swap
print("Approach 1 simple swap")
mylist = [23, 65, 19, 90]
print(mylist)

pos1, pos2 = 1, 3  # 65  90

mylist[pos1], mylist[pos2] = mylist[pos2], mylist[pos1]

print(mylist)

# Approach 2 : using inbuilt list.pop() function
print("Approach 2 : using inbuilt list.pop() function")
mylist = [23, 65, 19, 90]
print(mylist)

pos1, pos2 = 1, 3

first_element = mylist.pop(pos1)  # 65, then list don't have an element, see below
second_element = mylist.pop(pos2 - 1)  # 23, 19, 90
mylist.insert(pos1, second_element)
mylist.insert(pos2, first_element)

print(mylist)

# Approach 3 : using tuple
print("Approach 3 : using tuple")
mylist = [23, 65, 19, 90]
print(mylist)

pos1, pos2 = 1, 3

get = (mylist[pos1], mylist[pos2])  # 65 90
mylist[pos2], mylist[pos1] = get    # change

print(mylist)
