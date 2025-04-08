import datetime
# https://docs.python.org/3/library/datetime.html
date = datetime.date(2025, 1, 2)
today = datetime.date.today()
print(f"Random date: {date}")
print(f"Current date: {today}")

time = datetime.time(12,30,0)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m %D %Y") #read documentation for more commands

print(f"Current time: {now}")

target_datetime = datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")

