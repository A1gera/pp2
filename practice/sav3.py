import re
txt = input()
x = re.sub("abc","cba", txt)
print(x)
sec = open("Secondary.txt",'x')
for i in x:
    sec.write(i)