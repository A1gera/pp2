class Stry:
    def __init__(self):
        self.word = ""
        
    def getString(self):
        self.word = input()
        
    def printString(self):
        print(self.word)
word = Stry()
word.getString()
word.printString()  