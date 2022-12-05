##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
from random import randint
import smtplib

PLACEHOLDER = "[NAME]"
MY_EMAIL = "riderek92@gmail.com"
PASSWORD_GMAIL = "biakfcngewzztxqc"

def send_mail(to_email, mail_content):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL,password=PASSWORD_GMAIL)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject:Happy Birthday!\n\n{mail_content}")
    connection.close()

now = dt.datetime.now()
curr_month = now.month
curr_day = now.day

random_letter_num = randint(1,3)

# 2. Check if today matches a birthday in the birthdays.csv
data_csv = pandas.read_csv("birthdays.csv")
data = data_csv.to_dict(orient="records")

for record in data:
    name = record["name"]
    email = record["email"]
    month = record["month"]
    day = record["day"]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    if month == curr_month and day == curr_day:
        print("It it today!")
    
        with open(file=f"letter_templates/letter_{random_letter_num}.txt", mode="r") as file:
            letter_content = file.read()
            new_letter = letter_content.replace(PLACEHOLDER, f"{name}")
# 4. Send the letter generated in step 3 to that person's email address.
            send_mail(email, new_letter)




