from slacker import Slacker
import config as cf
import messages as msg

def Slack(warn, message, color, priority, date):
    channel  = cf.main_configuration['slack_channel']
    username = cf.main_configuration['slack_username']
    id       = cf.main_configuration['slack_id']
    slack = Slacker(id)

    attachment = {
            #"color": "#2eb886",
        	"title": warn,
        	"color": color,
	        "text": message,
            "fields": [
                {
                    "title": "Priority",
                    "value": priority,
                }
            ],
            "ts": date
    }

    attachment = [attachment]
    slack.chat_post_message(channel, message, attachments=attachment)
    
