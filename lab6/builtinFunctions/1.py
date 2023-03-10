#Write a Python program with builtin function to multiply all the numbers in a list
import math
list1 = []
n = int(input())
for i in range(n):
    i = int(input())
    list1.append(i)

res1 = math.prod(list1)

print(res1)