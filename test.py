import datetime
import time

today = datetime.date.today()

print ('{:%d.%m.%Y;%H:%M:%S}'.format(datetime.datetime.now()))
print (datetime.datetime.now().toordinal())
print (datetime.datetime.fromordinal(datetime.date.today().toordinal()))
i = int(time.time())
print (time.time())
print (datetime.datetime.fromtimestamp(time.time()))
print (datetime.datetime.fromtimestamp(i))