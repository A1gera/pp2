import re
txt = input()
x = re.findall("[A-Z][^A-Z]*",txt)
h = ' '.join(x)
print(h)