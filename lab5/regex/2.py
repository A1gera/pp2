import re
txt = input()
x = re.search("a.{1,2}b",txt)
print(x)