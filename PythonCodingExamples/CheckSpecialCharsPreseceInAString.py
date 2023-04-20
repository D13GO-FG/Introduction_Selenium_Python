import re

str1 = "Welcome@#$To^%^!Python^($Programming*!#*@$"
str2 = "Welcome To Python Programming"
regex = re.compile('[!@#$%^&*()]')
if regex.search(str2) is None:
    print("No special characters present in a string")
else:
    print("String contains special characters")
