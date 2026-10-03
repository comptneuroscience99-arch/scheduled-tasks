##################### Extra Hard Starting Project ######################
from multiprocessing.forkserver import connect_to_new_process

import pandas as pd
import datetime as dt
import smtplib as smtp
import random
import os



MY_EMAIL = str(os.environ.get("MY_EMAIL"))
MY_PASSWORD = str(os.environ.get("MY_PASSWORD"))
WHICH_LETTER = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

# 1. Update the birthdays.csv

update = input('Do you want to update? Type "Y" for yes' ).lower()

if update == 'y':
    name = input("Who's birthday to wish? " )
    email = input('And their email? ' )
    year = int(input('Not really important but which year? '))
    month = int(input('The month (in numbers, please!)? '))
    day = int(input('Which day? '))

    new_text = f'{name},{email},{year},{month},{day}\n'

    with open('birthdays.csv', 'a') as file:
        file.write(new_text)



df = pd.read_csv('birthdays.csv')

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_month = now.month
today_day = now.day

for index, row in df.iterrows():
    if  (row['month']==today_month) and (row['day'] == today_day):
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        name = row['name']
        letter = random.choice(WHICH_LETTER)
        with open(letter,'r') as file:
            letter = file.read()
            letter = letter.replace('[NAME]', name)

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtp.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row['email'],
                msg='Happy Birthday \n\n' + letter
            )









