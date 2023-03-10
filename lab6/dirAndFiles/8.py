import os
path = '/Users/aigerim/Desktop/labs/lab6/forremoving.txt'
isExist = os.path.exists(path)
print(isExist)
if isExist == True: 
    os.remove(path)