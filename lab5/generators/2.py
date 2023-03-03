def generator_comma(n):
    for i in range(0,n+1):
        if i%2==0:
            if(i == 0): continue
            yield i
n = int(input())
x = []
for gen in generator_comma(n):
    x.append(str(gen))
x = ', '.join(x)
print(x)