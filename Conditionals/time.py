# Lisa Rehm, Time of Day Python

import time 

#print(time.gmtime(0)) 
# This is the first instance of time

current =time.time()
# current time in seconds since gmtime

now = time.ctime(current)
print(now)
#current time we are used to seeing

local_time = time.localtime(current)
minute = local_time.tm_min
print(minute)
hour = local_time.tm_hour
print(hour)
# If we just want the hour