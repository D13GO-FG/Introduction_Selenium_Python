# 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    # if n == 0 or n == 1:
    #     return 1
    # else:
    #     return n * factorial(n - 1)     # 5 * 4 * 3 * 2 * 1

    # Approach 2
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)


num = 10
print("Factorial of", num, "is", factorial(num))
