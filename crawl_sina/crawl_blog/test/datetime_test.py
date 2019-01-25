import datetime 
import time

print 'date constructor ...'
print 'date constructor-> date.today()...'
date = datetime.date.today()
print 'date object method date.ctime()....'
print date.ctime()
print 'date object method date.timetuple()'
print date.timetuple()
print date.year
print date.month
print date.day
print 'date object methdod date.strftime()'
print date.strftime("%y/%m/%d")

print 'date constructor-> date.fromtimestamp()...'
date = datetime.date.fromtimestamp(time.time())
print date

print 'datetime constructor ...'
print 'datetime constructor->datetime.today()'
datetime_t = datetime.datetime.today()
print datetime_t 
print 'datetime constructor->datetime.now()'
datetime_t = datetime.datetime.now()
print datetime_t
print 'datetime constructor->datetime.strptime()'
datetime_t = datetime.datetime.strptime("2015-01-02", "%Y-%m-%d")
print datetime_t

print 'time constructor->time()'
print datetime.time()

print 'local_time ...'
local_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))
print local_time


print 'timedelta object ...'
print 'timedelta constructor->datetime.timedelta()'
print datetime.timedelta(days=1)
yesterday = datetime.date.today() - datetime.timedelta(days=1)
print type(yesterday)
print yesterday

yesterday = datetime.datetime.today() - datetime.timedelta(hours=5)
print yesterday
print yesterday.date()
print yesterday.time().strftime("%H:%M:%S")
print yesterday.strftime("%Y-%m-%d_%H:%M:%S")


