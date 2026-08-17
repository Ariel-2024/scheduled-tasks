##################### Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import os 
import smtplib
# 1. Update the birthdays.csv with your friends & family's details. 

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month,today_day)

data = pd.read_csv("birthdays.csv")
print(data)

# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
data_dict = data.to_dict("records")
print(data_dict)

print(data_dict[0]["name"])
birthdays_dict = {(row["month"],row["day"]):row  for row in data_dict}
print(birthdays_dict)


#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
if (today_month,today_day) in birthdays_dict:
    name = birthdays_dict[today].get("name")
    mail = birthdays_dict[today].get("email")

    files = os.listdir("letter_templates")
    file_random = random.choice(files)
    path = os.path.join("letter_templates",file_random)
    with open(path,"r") as file:
        txt_file = file.read()
    new_file = txt_file.replace("[NAME]",name)


    email = os.environ.get("MY_EMAIL")
    my_password = os.environ.get("MY_PASSWORD")
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=email,password=my_password)
    connection.sendmail(from_addr=email, to_addrs=mail, msg=new_file)
    connection.close()


