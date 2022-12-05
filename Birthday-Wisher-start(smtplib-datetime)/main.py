# import smtplib

# my_email = "riderek92@gmail.com"
# password_gmail = "biakfcngewzztxqc" ## hasło do app gmail
# password_yahoo = ""

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls() #secure connection with email provider
#     connection.login(user=my_email, password=password_gmail)
#     connection.sendmail(from_addr=my_email, to_addrs="shienzo@yahoo.com", msg="Subject:Hello\n\nThis is the body of my email.")

# import datetime as dt

# now = dt.datetime.now() #data i godzina w tej chwili
# year = now.year # tylko wyświetla rok

# date_of_birth = dt.datetime(year=1992, month=9, day=25)

import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "riderek92@gmail.com"
PASSWORD_GMAIL = "biakfcngewzztxqc"
current_day_of_week = dt.datetime.now().weekday() #pon=0, wt=1 ... ndz=6

if current_day_of_week == 0:
    with open(file="quotes.txt", mode="r") as file:
        all_quotes = file.readlines()
        random_quote = choice(all_quotes)    

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD_GMAIL)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="kamchoo@protonmail.com", msg=f"Subject: Random Quote of the Day.\n\n{random_quote}")