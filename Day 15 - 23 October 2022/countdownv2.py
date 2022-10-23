from tkinter import *
import datetime
from datetime import date

#starter code
root = Tk()
root.title('Countdown')
root.iconbitmap('countdown.png')
root.geometry("500x350")

#label
CHRISTMAS = Label(root, text="CHRISTMAS!", font=("Helvetica", 42), bg="black", fg="green")
CHRISTMAS.pack(pady=20, ipadx=10, ipady=10)

#Get today's dates
today = date.today()
#format date Sun - 08 Sep, 2013
f_today = today.strftime("%a - %d %b, %Y")

#today label
today_label = Label(root, text=f'Today is {f_today}')
today_label.pack(pady=20)

#Countdown
#days_in_year = 365
#today_day_number = int(today.strftime("%j"))
#xmas_date = datetime.date(2022, 12, 25)
#xmas_date.month * 100000000 +
#xmas_date.day * 1000000 +

#calulate days left in year
#days_left = days_in_year - today_day_number
xmas = datetime.date(2022, 12, 25) - datetime.date.today()
months = xmas / 30

countdown_label = Label(root, text=f'There Are Only {xmas} Days \n Left Xmas!! \n \n That is {months} Months', font=("Helvetica", 18))
countdown_label.pack(pady=20)


root.mainloop()
