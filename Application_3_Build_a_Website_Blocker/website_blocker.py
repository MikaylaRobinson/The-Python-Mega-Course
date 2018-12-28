import time
from datetime import datetime as dt 

# hosts_path = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=["www.facebook.com","facebook.com","www.imgur.com","imgur.com"]

def run_working_hours():
    print("Working hours...")
    with open(hosts_path,'r+') as file:
        content = file.read()
        for website in website_list:
            if website not in content:
                file.write(redirect + " " + website + "\n")

def run_outside_of_working_hours():
    with open(hosts_path, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()
    print("FUN!!!!!!")

def is_working_hours():
    return (dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() and
    dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23))

while True:
    if (is_working_hours()):
        run_working_hours()
    else:
        run_outside_of_working_hours()
    time.sleep(5)
        