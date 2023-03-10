#Write a Python program with builtin function that returns True if all elements of the tuple are true.
# smth = bool(input())
# x = []
# x.append(smth)
# print(x)
# tuple23 = tuple(x)
# ans = all(tuple23)
# # print(ans)
tupple = (True, 1, True)
tupleee = (False, False, True)
print(all(tupleee))
print(all(tupple))