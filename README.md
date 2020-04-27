## Get informed about updated COVID-19 cases in your country simply from your terminal
### Script Output
<p align = "center">
<img src="Images/1.png">
</p>


## What does this script do ?

    1) Displays live count of COVID-19 cases in your Country.
    2) Displays number of New Cases wrt Previous update
    3) Plays Sound Notification when new Cases are Detected     ** Disabled By Default  To Enable : Uncomment Line 33 
    4) Sends A Slack Message Alert                              ** Disabled By Default  

## Procedure 

    1) Download the script 
    2) Run The Script in terminal
        - python3 covid_updates.py CountryName SoundPath
    3) To run script in background with slack and music notifications , run in terminal 
        - nohup sh updates.sh &&
 
## Installing Dependencies 
    
    -pip install playsound

### ** To Enable Slack Notification 

    - Get the Slack Access token url and modify the script with your access token url and uncomment following lines [12,27,28,29]

        ex- https://hooks.slack.com/services/xxxxxxxxx
