num1 = input("Enter num1 value:")
num2 = input("Enter num2 value:")

print("Values of num1 before swapping:", num1)
print("Values of num2 before swapping:", num2)

# # Approach 1
# temp = num1
# num1 = num2
# num2 = temp

# Approach 1
num1, num2 = num2, num1

print("Values of num1 after swapping:", num1)
print("Values of num2 after swapping:", num2)
