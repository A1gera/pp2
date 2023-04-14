import os
txt = '/Users/aigerim/Desktop/labs/practice'
cntTxt = 0
cntPy = 0
for x in os.listdir(txt):
    if x.endswith(".txt"): cntTxt = cntTxt+1
    elif x.endswith(".py"): cntPy = cntPy+1
for i in os.listdir(txt):
    if os.path.isfile(os.path.join(txt, i)) and i.endswith(".txt"):
        os.remove(i)
print(cntTxt)
print(cntPy)