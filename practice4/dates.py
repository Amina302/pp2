from datetime import datetime, timedelta
#1
x =datetime.now()
five_days_ago=x-timedelta(days=5)
print (five_days_ago)
print()

#2
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday)
print(today)
print(tomorrow)
print()

#3
dt = datetime.now()
no_microseconds = dt.replace(microsecond=0)
print(no_microseconds)
print()

#4
date1 = datetime(2025, 2, 20, 12, 0, 0)
date2 = datetime(2025, 2, 22, 12, 0, 0)
difference = date2 - date1
print(difference.total_seconds())
