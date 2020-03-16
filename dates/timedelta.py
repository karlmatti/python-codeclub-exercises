'''
Write a function time_diff(timestamp1, timestamp2) that returns the absolute
difference of two timezone aware datetime objects in seconds

Return an integer rounded to full seconds. E.g., when there are microseconds
in the resulting difference round them up.

'''
import pytz
def time_diff(timestamp1, timestamp2):
    print(timestamp1)
    print(timestamp2)

import time
ts = time.time()
print(ts) # 1580010747.0889.
