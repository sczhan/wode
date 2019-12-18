import datetime
import time

a = time.ctime()
b = datetime.datetime.now()
d = b.timetuple()
c = time.mktime(d)
e = str(b.microsecond)[0:3]
f = b.microsecond
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)