## Time and DateTime ##

## should be storing dates as UTC!
## UTC - Coordinated Universal Time

# import time

# print(time.gmtime(0))   # going back to start date
#
# print(time.localtime())
# print(time.localtime(time.time()))
#
# print(time.time())      # seconds since start of epoch, 1970

# time_here = time.localtime()
# print(time_here)
# print("Year: ", time_here[0], time_here.tm_year)       # both ways work the same: [0] and .tm_year
# print("Month: ", time_here[1], time_here.tm_mon)
# print("Day: ", time_here[2], time_here.tm_mday)

import time
# from time import time as my_timer
from time import perf_counter as my_timer       # best way to measure elapsed time
# from time import monotonic as my_timer
# from time import process_time as my_timer     # to measure how much time CPU spends on a process
import random
#
# input("Press Enter to Start")
#
# wait_time = random.randint(1,6)
# time.sleep(wait_time)
# start_time = my_timer()
# input("Press Enter to Stop")
#
# end_time = my_timer()
#
# print("Started at " + time.strftime("%X", time.localtime(start_time)))  # strftime = string from time
# print("Ended at " + time.strftime("%X", time.localtime(end_time)))
#
# print("Your reaction time was {} seconds".format(end_time - start_time))
#
# print('=' * 80)

## Challenge ##

print("time():\t\t\t", time.get_clock_info('time'))
print("perf_counter():\t", time.get_clock_info('perf_counter'))
print("monotonic():\t", time.get_clock_info('monotonic'))
print("process_time():\t", time.get_clock_info('process_time'))