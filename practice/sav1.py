def generator_fives(n):
    for i in range(0,n):
        if i % 5 == 0:
            yield i
n = int(input())
for m in generator_fives(n):
    print(m)