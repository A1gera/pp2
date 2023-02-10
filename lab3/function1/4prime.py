def getPrime():
    for i in nums:
        c = 0
        for j in range(1, i):
            if i % j == 0:
                c += 1
        if c == 1:
            pnums.append(i)
    print(pnums)
nums = []
pnums = []
rang = int(input())
for i in range (rang):
    nums.append(int(input()))
getPrime()