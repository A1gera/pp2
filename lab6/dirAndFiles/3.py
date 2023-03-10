import os
path = '/Users/aigerim/Desktop/labs/lab4/math/1.py'
isExist = os.path.exists(path)
print(isExist)
file_name = os.path.basename(path)
print(file_name)
dirr = os.path.dirname(path)
print(dirr)