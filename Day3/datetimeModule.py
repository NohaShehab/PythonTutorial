#python can handle datetime in several ways
#there is a popular module in python called time to handle working with times

import time

ticks = time.time()
print(ticks) #returned with time calculated from 1 Jan 1970 in secs


#time tuple consists of 9 fields starts with 
# 1- 4-digit year
# 2- Month 1 to 12
# 3- day 1 to 31
# 4- Hour 0 to 23
# 5- Minute 0 to 59
# 6- Second 0 to 56 
# 7- Day of week 0 to 6 
# 8- Day of year 1 to 365
# 9- Daylight saving -1 0 1 -1 0

nowTime = time.localtime(time.time())
print(nowTime)


# to format time asctime
nowTime = time.asctime(time.localtime(time.time()))
print(nowTime)


# Calender 
import calendar  
yy = 1992
mm = 6
# display the calendar  
print(calendar.month(yy, mm))  

print (calendar.calendar(2020, 2, 1, 6))  

