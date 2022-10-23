# importing the datetime module
import datetime

# Getting todays date and time using now() of
# datetime class
current_date = datetime.datetime.now()

# Printing the current_date as the date object itself.
print("Original date and time object:", current_date)

# Retrieving each component of the date
# i.e year,month,day,hour,minute,second and
# Multiplying with multiples of 100
# year - 10000000000
# month - 100000000
# day - 1000000
# hour - 10000
# minute - 100
print("Date and Time in Integer Format:",
      current_date.year*10000000000 +
      current_date.month * 100000000 +
      current_date.day * 1000000 +
      current_date.hour*10000 +
      current_date.minute*100 +
      current_date.second)# Write your code here :-)
