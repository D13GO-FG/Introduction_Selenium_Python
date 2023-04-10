# Tuple Packing
A = 10, 20, 30

print(A)
print(type(A))

# Tuple Unpacking
A = 1, 2, 3, 4
a, b, c, d = A

print(d)

a = [10, 20, 30]
for i in a:
    print("in for loop")
else:
    print("in else block")

# initializing a with range()
a = range(1, 10000)

print("The return type of range() is : ")
print(type(a))
print(a)

a = [1, 2, 3, 4]  # List
print(a[-1])  # 4
print(a[-2])  # 3

b = (1, 2, 3, 4)  # Tuple
print(b[-1])  # 4
print(b[-2])  # 3

# 26) What is slice notation in Python to access elements in an iterator?
a = [100, 200, 300, 400, 500, 600, 700, 800]

print(a[3:])  # Prints the values from index 3 till the end [400, 500, 600, 700, 800]
print(a[3:6])  # Prints the values from index 3 to index 6. [400, 500, 600]
print(a[2::2])  # Prints the values from index 2 till the end of the list with step count 2. [300, 500, 700]

# 27) How do you convert a list of integers to a comma separated string?
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
numbers = ','.join(str(i) for i in a)
print(numbers)

# 28) What is the difference between Python append () and extend () functions?
a = [1, 2, 3, 4, 5]
b = [6, 7, 8]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6, 7, 8]
c = ['a', 'b']
a.append(c)
print(a)  # [1, 2, 3, 4, 5, 6, 7, 8, ['a', 'b']]
str = "welcome"
print(str[1:3])  # el
print(str[:6])  # welcom
print(str[4:])  # ome
print(str[1:-1])  # elcom #elimate 1 char from end
print(str[1:-2])  # elco #eleminate 2 chars from end

# 30) How do you create a list which is a reverse version on another list in Python?
a = [10, 20, 30, 40, 50]
print(a)
b = list(reversed(a))  # [10, 20, 30, 40, 50]
print(b)  # [50, 40, 30, 20, 10]

# 31) What is a dictionary in Python?
# Retrieving, modifying and adding elements in the dictionary
friends = {'tom': '111-222-333', 'jerry': '666-33-111'}
print(friends)  # {'tom': '111-222-333', 'jerry': '666-33-111'}

# Retrieving elements from the dictionary
print(friends['tom'])  # 111-222-333

# Adding elements into the dictionary
friends['bob'] = '888-999-666'
print(friends)  # {'tom': '111-222-333', 'jerry': '666-33-111', 'bob': '888-999-666'}

# Modify elements into the dictionary
friends['bob'] = '888-999-777'
print(friends)  # {'tom': '111-222-333', 'jerry': '666-33-111', 'bob': '888-999-777'}

# Delete element from the dictionary
del friends['bob']
print(friends)  # {'tom': '111-222-333', 'jerry': '666-33-111'}

# 34) names = [‘john’, ‘fan’, ‘sam’, ‘megha’, ‘popoye’, ’tom’, ‘jane’, ‘james’,’tony’]Write one line of code to get a
# list of names that start with character ‘j’?
names = ['john', 'fan', 'sam', 'megha', 'popoye', 'tom', 'jane', 'james', 'tony']
jnames = [name for name in names if name[0] == 'j']  # One line code to filter names that start with ‘j’
print(jnames)

# 36) a = “this is a sample string with many characters”
# Write a Python code to find how many characters are present in this string?
a = "this is a sample string with many characters"
print(len(set(a)))  # 16

# 46). How can you randomize the items of a list in place in Python?
from random import shuffle

x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)

# 47). Write a sorting algorithm for a numerical dataset in Python.
list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print(list)


