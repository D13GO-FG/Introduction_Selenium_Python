# Input : List = [3, 2, 4]
# Output : 24
# Explanation : 3*2*4 = 24

# Method 1: Traversal
myList = [3, 2, 4]
result = 1
for x in myList:
    result = result * x
print(result)

# # Method 2: using numpy.prod() * Install numpy package
# import numpy
# myList = [3, 2, 4]
# result = numpy.prod(myList)
# print(result)
