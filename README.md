# Eagle Eye
- Monitor your server resources (cpu , memory , disks and swap)<br/>
- Monitor your domains uptime<br/> 
- Monitor ssl expire dates<br/>
- Send alerts to slack<br/>

# Installation
1. git clone https://github.com/warrengalyen/eagleeye.git
2. pip install -r requirements.txt

# Usage
- Set your slack credentials in main.yaml file<br/>
- Set your rules in yaml files inside rules directory<br/>
- Add Eagle Eye to the running crons<br/>
"* * * * *" cd /path-to/eagle_eye/ && python eagle_eye.py > /tmp/eagle_eye.log 2>&1