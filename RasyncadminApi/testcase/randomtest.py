import requests
import json
import time
url='http://127.0.0.1:8090/api'
param={"UK": "0Jy5NLeNJP5plYROv6zAmMd1DwknVE4V55wWGqboyVW2Qa30EZ48XBKjrG9xR4lwbR4BMXN3VJpKWyxaeE1jzmq651jXLpykQTrZ983G617926YGrQ5ol0vAkZPD8wOL",
"action":"login",
"device": "",
"id": 1543386059,
"module": "WEBADMIN",
"token": "",
"version": "3.0.3.2"
}
param1=json.dumps(param)
print(param1)
r=requests.post(url,data=param1)
n=json.loads(r.text)
print(n)
# print(str(n['result']))
# aa=time.time()
# print(int(aa))

