# 5! = 1 * 2 * 3 * 4 * 5 = 120

factorial = 1
num = 5

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
