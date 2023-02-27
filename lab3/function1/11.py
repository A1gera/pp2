class Str():
    def __init__(self):
        self.word = ''
    def mak(self,word):
        res = ""
        for i in range(len(word)):
            if i%2==0: 
                res += word[i]
        return res
word = input()
cl = Str()
print(cl.mak(word))