# add Boti-Test to prviate Slack channel

# ref: https://www.youtube.com/watch?v=KJ5bFv-IRFM&t=784s
# in CLI:
# pip install slackclient
# pip isntall python-dotenv
# pip install flask
# pip install slackeventsapi

# ref: https://www.youtube.com/watch?v=6gHvqXrfjuo
# download ngrok, exract file
# launch ngrok
# ngrok http 5000
# copy forwarding http url
# Slack API > Your Apps > "Boti-Test" > Event Subscriptions > Enable Events ON > paste URL with "/slack/events" at the end > Verify > Save 

import slack
import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, make_response, Response
from slackeventsapi import SlackEventAdapter
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import sys

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

# Integrate with Ravi's code to define list of calendar events for current day
list_events = ["MSA Meeting","Columbia Weekly Review","Internal CC Meeting"]
count_events = len(list_events)

# CHANGE THIS TO THE CHANNEL YOU ARE TESTING IN
channel_test = '#bot-test-jacob'
channel_test_id = 'C01NVQA3FFX'

# intro message asking if user wants to track time
client.chat_postMessage(
    channel=channel_test,
    blocks= [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*Boti here!* :robot_face: Let's track your time! :timer_clock: \n\nReply with *'Track'* to coninute or *'Bye'* to cancel..."
			}
		}
	]
)

# accepts user's response continuously. if statements will control bot's reaction to user
@slack_event_adapter.on('message')
def message(payload):
    # uncomment below to see out from user (can be used to get user_id, channel_id, etc.)
    # print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    # filters response to only use non-bot and only in test channel
    if ((BOT_ID != user_id) and (channel_id == channel_test_id)):
        
        # user responds they do want to track time
        if (text.lower() == 'track'):
            client.chat_postMessage(
                channel=channel_test,
                text="yes, track"
            )

        # user responds they dont want to track time
        if (text.lower() == 'bye'):
            client.chat_postMessage(
                channel=channel_test,
                text='Rude. Thanks anyway. Have a great day. Boti out!'
            )
        
        if (text.lower() == 'kudos'):
            client.chat_postMessage(
                channel=channel_test,
                blocks= [
		            {
			            "type": "section",
			            "text": {
			            	"type": "mrkdwn",
			            	"text": "<!channel> *Jacob* tracked his time for today! :clap:"
			            }
		            }
	            ]
            )
               
        # error in response if no active input detected
        else:
            client.chat_postMessage(
                channel=channel_test,
                blocks= [
		            {
			            "type": "section",
			            "text": {
			            	"type": "mrkdwn",
			            	"text": ":warning: *Error: You confused Boti* :white_frowning_face: \n\nBoti does not yet support typos... unless you fund this project :wink:"
			            }
		            }
	            ]
            )

# debugger which coincidently causes messages to send twice, will not work without it though
if __name__ == "__main__":
    	app.run(debug=True)
