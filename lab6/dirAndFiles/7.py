txt_file = '/Users/aigerim/Desktop/labs/lab6/demo.txt'
f = open(txt_file, 'r')
sec = open("Secondary.txt",'x')
for i in f:
    sec.write(i)