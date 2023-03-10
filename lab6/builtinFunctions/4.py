#Write a Python program that invoke square root function after specific milliseconds.
import math
import time
num = int(input())
smtime = int(input())
time.sleep(smtime/1000)
print(math.sqrt(num))