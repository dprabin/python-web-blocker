import time
from datetime import datetime as dt

hosts_path = r"c:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","live.com","hotmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Workiong Hours")
    else:
        print("Fun Hours")
    time.sleep(5)
