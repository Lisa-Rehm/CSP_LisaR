# Lisa Rehm, Time of Day Python

import time 

current =time.time()
local_time = time.localtime(current)
minute = local_time.tm_min
hour = local_time.tm_hour
print(hour)


if hour <= 5:
    print("Go to bed... please!!\n")
elif hour <= 11:
    print("Good Morning, are you well rested?!\n")
elif hour == 12:
    print("Good day! I'm giving you one hour to find your shadow.\n")
elif hour <= 16:
    print("Good afternoon! Don't go outside if it's summer, it's way too hot.\n")
elif hour <= 19:
    print("Good evening! Now you can go outside, have fun!\n")
elif hour <= 23:
    print("Good night! Please go to bed at a reasonable hour.\n")
else:
    print("That is not a time on this planet...\n")

