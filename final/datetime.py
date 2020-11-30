from datetime import datetime, timedelta

now = datetime.now()

alarmtime = datetime(now.year, now.month, now.day, 19, 31, 40)
#now.day를 받을때, now.hour보다 alarmtime의 hour이 더 작으면 day+1
print((alarmtime - now).seconds)
