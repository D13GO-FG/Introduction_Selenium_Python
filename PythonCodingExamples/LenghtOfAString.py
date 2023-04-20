# input : welcome
# output : 7

# Method1 : using for loop
str = "welcome"
counter = 0
for i in str:
    counter = counter + 1
print(counter)

# Method 2 : using while loop and slicing
str = "welcome"
counter = 0
while str[counter:]:  # 1 : 6, ... , 6 : 6
    counter = counter + 1
print(counter)

# Method 3 : using built-in function len()
str = "welcome"
print(len(str))

# Method 4 : using join and count
str = "welcome"
random_str = "X"
print(random_str.join(str))  # wXeXlXcXoXmXe
print(random_str.join(str).count(random_str))  # 6
print(random_str.join(str).count(random_str) + 1)  # 7  length of a string


