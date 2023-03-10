import os
path = '/Users/aigerim/Desktop/labs/lab4/math/2.py'
isExist = os.path.exists(path)
print(isExist)
openedPath = open(path, 'rt')
print(openedPath.readable())
print(openedPath.writable())