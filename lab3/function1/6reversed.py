def wordRev(b):
    a = b.split()
    a.reverse()
    return  ' '.join(a)

b = input()

print(wordRev(b))