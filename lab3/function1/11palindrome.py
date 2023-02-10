
def pal_or_not(word):
    if word == word[::-1]:
        return True
    else:
        return False
word = input()
print(pal_or_not(word))
    
    