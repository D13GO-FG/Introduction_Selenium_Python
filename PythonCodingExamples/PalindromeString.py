# Method #1
# 1) find reverse of string
# 2) check if reverse and original are same or not.

s = input("Enter a string: ")

print(s[:])  # abcde
print(s[0:5])  # abcde
print(s[0:5:1])  # abcde
print(s[::])  # abcde

rev_str = (s[::-1])  # edcba reverse string

if rev_str == s:
    print("Palindrome")
else:
    print("Not Palindrome")

