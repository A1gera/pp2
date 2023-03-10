#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
txt = input()
upper = 0
lower = 0
for i in range(len(txt)):
    if txt[i].isupper():
        upper = upper + 1
    else:
        lower = lower + 1

print(upper, lower)