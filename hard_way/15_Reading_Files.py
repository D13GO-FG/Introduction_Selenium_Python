from sys import argv
script, filename = argv

txt = open("15_sample.txt")

print(f"Here's your life {filename}")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
