import requests
import json
import datetime
from subprocess import call
import time;
#To listen 
#from gtts import gTTS
bigarray=[]
send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
lati = j['latitude']
longi = j['longitude']
parameters = {"lat": lati, "lon": longi}
respo = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
a = respo.content
result = json.loads(a)
def IssTime():
    for i in range(len(result['response'])):
        b = result["response"][i]["risetime"]
        bigarray.append(b)

    return bigarray

import time,datetime
def localTime():
     c=time.time()
     d=int(c)
     return d

def timer():
    IssTime()
    for i in range(len(bigarray)):
        d=int(bigarray[i])-int(localTime())
        print datetime.datetime.fromtimestamp(
           int(d)
        ).strftime('%H:%M:%S')
timer()
#d=print datetime.datetime.fromtimestamp(
#         int(d)
#        ).strftime('%H:%M:%S')
#tts = gTTS(text=d, lang ='en')
#tts.save("iss.mp3")
#os.system("Rhythmbox iss.mp3")
#call(["espeak",c])
