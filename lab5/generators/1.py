def generator_squares(n):
    x = 0
    for i in range(1,n):
        x = i*i
        yield x

n = int(input())
for x in generator_squares(n+1):
    print(x)
