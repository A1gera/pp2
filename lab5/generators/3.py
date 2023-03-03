def generator_div(n):
    for i in range(0,n):
        if i % 12 == 0:
            yield i
n = int(input())
for m in generator_div(n):
    print(m)

        