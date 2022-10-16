#Day countdown timer

import datetime
#from rich import print

#variable for countdown to
NEW_YEAR = datetime.datetime(2022, 10, 17)#year, month, date

#the time we surpass if we are in the date to
DELTA = datetime.timedelta(microseconds=-0.00000001)

#code to repeat every 1 second
while True:
    time_until_ny = NEW_YEAR - datetime.datetime.now()
    #seconds_left = time_until_ny.total_seconds()
    #hours, remainder = divmod(seconds_left, 3600)
    #minutes, seconds = divmod(remainder_60)

    #check if time till ny is less then delta
    if time_until_ny < DELTA:
        print("Happy New Year!!!")
        #to end repitition
        break
    #print out time till ny
    else:
        print(time_until_ny)
        #print(f"{int(hours)}:{int(minutes):02d}:{int(seconds):02d}")  ##hours:mins,seconds
    #wait a second
    time.sleep(1)

