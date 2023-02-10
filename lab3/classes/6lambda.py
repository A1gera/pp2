
def isPrime(ls):
    return list(filter(lambda x: all(x%i != 0 for i in range(2, x)) and x>= 2, ls))
print(isPrime([1,2,3,4,5,6,7,8,9]))