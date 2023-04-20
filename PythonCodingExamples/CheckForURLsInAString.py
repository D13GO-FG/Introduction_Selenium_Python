import re
str1 = "I'm blogger at https://urlregex.com/"
str2 = "Wikipedia: https://en.wikipedia.org/wiki/The_Tetris_Company"
str3 = "Wikipedia: https://en.wikipedia.org/wiki/Main_Page and with Tetris: https://en.wikipedia.org/wiki/Tetris"

# https://urlregex.com/
# http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+

url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str3)
print(url)