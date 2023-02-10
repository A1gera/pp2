
def solve(numheads,numlegs):
    chica = 0
    rabba = 0
    if(numheads<numlegs and numlegs % 2==0):
        rabba = (numlegs - 2*numheads)/2
        chica = numheads - rabba
    else : print('No solution')
    return(int(chica),int(rabba))

numheads = int(input())
numlegs = int(input())
print(solve(numheads, numlegs))