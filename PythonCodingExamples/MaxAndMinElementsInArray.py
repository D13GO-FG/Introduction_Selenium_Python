# Input : arr[] = {10, 20, 4}
# Output: 20
# Output: 4

arr = [30, 20, 15, 40, 10]

# Finding max element
max = arr[0]
n = len(arr)

for i in range(1, n):
    if arr[i] > max:
        max = arr[i]
print("Maximum element is: " + max)

# Finding min element
arr = [30, 20, 15, 40, 10]
min = arr[0]
n = len(arr)

for i in range(1, n):
    if arr[i] < min:
        min = arr[i]
print("Minimum element is: " + max)
