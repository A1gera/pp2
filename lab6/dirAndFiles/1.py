import os
txt = '/Users/aigerim/Desktop/labs/lab6'
#only directories
for i in os.listdir(txt):
    if os.path.isdir(os.path.join(txt, i)):
        print(i)
#only files
for x in os.listdir(txt):
    if x.endswith(".txt") or x.endswith(".py"):
        print(x)
#files and all directories
print(os.listdir(txt))