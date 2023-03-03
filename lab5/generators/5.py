def generator_down(n):
    for i in range(n,-1,-1):
        yield i
n = int(input())
for h in generator_down(n):
    print(h)