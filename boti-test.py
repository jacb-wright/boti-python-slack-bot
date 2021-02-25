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

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['31b87437c2a6aff6d7c7a119d6c82c78'], '/slack/events', app)

client = slack.WebClient(token=os.environ['xoxb-4004473389-1779407041846-FjKM0OP48cxqf9HNFULPu5Mf'])
BOT_ID = client.api_call("auth.test")['user_id']

# Integrate with Ravi's code to define list of calendar events for current day
list_events = ["MSA Meeting","Columbia Weekly Review","Internal CC Meeting"]
count_events = len(list_events)

# CHANGE THIS TO THE CHANNEL YOU ARE TESTING IN
channel_test = '#bot-test-jacob'

client.chat_postMessage(
    channel=channel_test,
    text="It's time to track your time! Reply 'Fine.' to continue or 'Go away!' to cancel"
)

@slack_event_adapter.on('message')
def message(payload):
    # uncomment the below to view the JSON payload retrieved
    # print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    # locate channel_id using print(payload) in line 52. copy and paste to channel_id == ''
    if ((BOT_ID != user_id) and (channel_id == 'C01NVQA3FFX') and (text == 'Fine.')):
        track_time = 'Yes'

        while track_time == 'Yes':
            client.chat_postMessage(
                channel=channel_test,
                text='This is where the code will go to ask about each list item and track the user's input. Blank until I get the important stuff working.'
            )
            track_time = 'No'
        
    # locate channel_id using print(payload) in line 52. copy and paste to channel_id == ''
    if ((BOT_ID != user_id) and (channel_id == 'C01NVQA3FFX') and (text == 'Go away!')):
        client.chat_postMessage(
        channel=channel_test,
        text='Geez, okay. Thanks anyway. Have a great day. Boti out!'
        )
        quit()

    # locate channel_id using print(payload) in line 52. copy and paste to channel_id == ''
    if ((BOT_ID != user_id) and (channel_id == 'C01NVQA3FFX') and (text != 'Go away!' or 'Fine.')):
        client.chat_postMessage(
        channel=channel_test,
        text='Error. You confused Boti. Boti does not yet support typos... unless you fund this project ;)...'
        )
        quit()


if __name__ == "__main__":
    	app.run(debug=True)
