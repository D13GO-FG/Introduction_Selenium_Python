# Input : List = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# x = 10
# Output : 3
# 10 appears three times in given list.

# Method 1: using loop
myList = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
count = 0

for element in myList:
    if element == x:
        count += 1
print("{} has occurred {} times".format(x, count))

# Method 2: using count()
myList = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
print("{} has occurred {} times".format(x, myList.count(x)))

# Method 3: using Counter()
from collections import Counter

myList = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
dic = Counter(myList)  # { 5 : 1, 6 : 1, 7 : 1, 10 : 3, ...}
print("{} has occurred {} times".format(x, dic[x]))
