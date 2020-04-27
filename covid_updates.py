import pandas as pd
import requests
from datetime import datetime
import json
from playsound import playsound
import time 
import sys 
import json
z=sys.argv[1]
url= "https://google.com/covid19-map/?hl=en"
r= requests.get(url)
df= pd.read_html(r.text)[0]
num=int(df.loc[df['Location']==z,"Confirmed"])
print("Current Cases: ",num)
i=0
while True:
    i+=1
    r= requests.get(url)
    df= pd.read_html(r.text)[0]
    num_new=int(df.loc[df['Location']==z,"Confirmed"])
    if num_new > num:
        now=datetime.now()
        new_cases=num_new-num
        timez= now.strftime("%m-%d %H:%M:%S")
        print("----------------------")
        print("Previous Cases",num)
        print("Current Cases: ",num_new)
        print("New Cases Found : \n",num_new-num)
        playsound('alarm.mp3')
        num=num_new
        del(df)
        del(r)
    else:
        print("----------------------")
        print("Previous Cases",num)
        print("Current Cases: ",num_new)
        print("New Cases:",num_new-num)
        print("Number of times data refreshed:",i)
        del(df)
        del(r)
        time.sleep(300)
        
