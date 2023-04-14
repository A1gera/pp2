import os, datetime
os.mkdir("zashita")
path = '/Users/aigerim/Desktop/labs/zashita'
x = open("D:///Users/aigerim/Desktop/labs/zashita/11.03.23.txt", 'x')
file = "/zashita/11.03.23.txt"
path = os.getcwd()+file
fp = open(path, 'r+')
y = datetime.datetime.now().strftime("%d.%m.%y")
x.write(y)
x.close()