import re

text = open('mytest.txt', 'r').read()

x = input("Which word you want to find?: ")

result = re.findall(x, text)

print(result)


