#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
txt = list(input())
txtx = list(reversed(txt))
if  txtx == txt:
    print("Yeahh, it's palindrome")
else: print("NOOO, it's not a palindrome")