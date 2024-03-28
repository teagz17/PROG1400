from datetime import datetime, timedelta

# decimal time represents seconds since unix epoch
decimal_time = 1711629855
decimal_time_offset = -10800 # halifax
epoch = datetime(1970, 1, 1) # unix epoch
timestamp = epoch + timedelta(seconds=decimal_time)
# un-comment for troubleshooting
#print(f"{timestamp}")
current_time = timestamp + timedelta(seconds=decimal_time_offset)
#print(f"{current_time.day}")
#print(f"{current_time.month}")
#print(f"{current_time.year}")

#if current_time.weekday() == 0:

# data format codes
# https://www.w3schools.com/python/gloss_python_date_format_codes.asp

weekday = current_time.strftime("%A")
print(f"{current_time.strftime('%A %m-%d-%Y %H:%M:%S')}")
print(f"{current_time.strftime('%A %B %d, %Y %H:%M')}")
print(f"{current_time.strftime('%a %b %d, %Y %H:%M %p')}")