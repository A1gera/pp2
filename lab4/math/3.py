#Write a Python program to calculate the area of regular polygon
import math
n = int(input("Input number of sides: "))
i = int(input("Input the length of a side: "))
x = math.pi
print("The area of the polygon is: ", int((((n/4) * math.pow(i, 2)) * (math.cos(x/n)/math.sin(x/n)))))