import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path = r"c:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","live.com","hotmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Workiong Hours")
        with open(hosts_temp,"r+") as fh:
            content = fh.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    fh.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp,"r+") as fh:
            content=fh.readlines()
            fh.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    fh.write(line)
            fh.truncate()
        print("fun hours")

    time.sleep(5)
