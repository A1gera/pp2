def generator_squares(a,b):
    x = 0
    for i in range(a,b):
        x = i*i
        yield x

a = int(input())
b = int(input())
for jj in generator_squares(a,b):
    print(jj)