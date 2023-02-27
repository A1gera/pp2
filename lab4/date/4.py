import datetime
a = datetime.datetime(2013,12,30,23,59,59)
b = datetime.datetime.now()

print(int((b-a).total_seconds()))