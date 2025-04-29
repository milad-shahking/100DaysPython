import datetime

newYear = datetime.date(2025,1,1)
print(newYear.day)


myBerthDay = datetime.datetime(1991,11,4)
print(myBerthDay.day)

now = datetime.datetime.now()
sen = now - myBerthDay
print(sen)
print(sen.days)



print(now.ctime())


