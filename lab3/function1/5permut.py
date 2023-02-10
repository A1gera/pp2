from itertools import permutations

def strPermut():
    word = input()
    perm = permutations(word)
    for i in list(perm):
        print(i)

strPermut()