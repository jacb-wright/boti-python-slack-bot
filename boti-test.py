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
import random
import pickle

# unpickle Ravi's code
#with open('cal2csvnew2_final.py', 'rb') as filehandle:
#    my_list_events=pickle.load(filehandle)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'], '/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']


# Integrate with Ravi's code to define list of calendar events for current day
list_events = ["MSA Meeting","Columbia Weekly Review","Internal CC Meeting","e4","e5"]
#list_events = my_list_events
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
        
    # DO YOU WANT TO TRACK TIME - YES
        # user responds they do want to track time
        if ((text.lower() == 'track') or (text.lower() == 'done')):    
            
            if (count_events == 5):
                event5 = list_events[4]

                client.chat_postMessage(
                    channel=channel_test,
                    blocks= [
		                {
			                "type": "section",
			                "text": {
			                	"type": "mrkdwn",
			                	"text": "Do you want to track *'"+event5+"'* in your timecard?"
			                 }
		                }
	                ]
                )
                
                @slack_event_adapter.on('message')
                def message2(payload):
                    event2 = payload.get('event', {})
                    channel_id2 = event2.get('channel')
                    user_id2 = event2.get('user')
                    text2 = event2.get('text')

                    # filters response to only use non-bot and only in test channel
                    if ((BOT_ID != user_id2) and (channel_id2 == channel_test_id)):
                
                        if (text2.lower() == 'yes'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "How many *minutes* do you want to track?"
			                             }
		                            }
	                            ]
                            )

                            @slack_event_adapter.on('message')
                            def message3(payload):
                                event3 = payload.get('event', {})
                                channel_id3 = event3.get('channel')
                                user_id3 = event3.get('user')
                                text3 = event3.get('text')

                                # filters response to only use non-bot and only in test channel
                                if ((BOT_ID != user_id3) and (channel_id3 == channel_test_id)):

                                   if (int(text3) > 0) and (int(text3) < 500):
                                        client.chat_postMessage(
                                            channel=channel_test,
                                            blocks= [
		                                        {
			                                        "type": "section",
			                                        "text": {
			                                        	"type": "mrkdwn",
			                                        	"text": "What *company* is this event for? (Reply with *'Done'* after you send this)\n\n_Is this event is non-billable, please enter *'Computacenter'*._"
			                                        }
		                                        }
	                                        ]
                                        )
                                        global count_events
                                        count_events = 4
            
                        if (text2.lower() == 'no'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "*Noted.* Reply *'Track'* to track another"
			                             }
		                            }
	                            ]
                            )
                            global count_events
                            count_events = 4

            if (count_events == 4):
                event4 = list_events[3]

                client.chat_postMessage(
                    channel=channel_test,
                    blocks= [
		                {
			                "type": "section",
			                "text": {
			                	"type": "mrkdwn",
			                	"text": "Do you want to track *'"+event4+"'* in your timecard?"
			                 }
		                }
	                ]
                )
                
                @slack_event_adapter.on('message')
                def message2(payload):
                    event2 = payload.get('event', {})
                    channel_id2 = event2.get('channel')
                    user_id2 = event2.get('user')
                    text2 = event2.get('text')

                    # filters response to only use non-bot and only in test channel
                    if ((BOT_ID != user_id2) and (channel_id2 == channel_test_id)):
                
                        if (text2.lower() == 'yes'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "How many *minutes* do you want to track?"
			                             }
		                            }
	                            ]
                            )

                            @slack_event_adapter.on('message')
                            def message3(payload):
                                event3 = payload.get('event', {})
                                channel_id3 = event3.get('channel')
                                user_id3 = event3.get('user')
                                text3 = event3.get('text')

                                # filters response to only use non-bot and only in test channel
                                if ((BOT_ID != user_id3) and (channel_id3 == channel_test_id)):

                                   if (int(text3) > 0) and (int(text3) < 500):
                                        client.chat_postMessage(
                                            channel=channel_test,
                                            blocks= [
		                                        {
			                                        "type": "section",
			                                        "text": {
			                                        	"type": "mrkdwn",
			                                        	"text": "What *company* is this event for? (Reply with *'Done'* after you send this)\n\n_Is this event is non-billable, please enter *'Computacenter'*._"
			                                        }
		                                        }
	                                        ]
                                        )
                                        global count_events
                                        count_events = 3
            
                        if (text2.lower() == 'no'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "*Noted.* Reply *'Track'* to track another"
			                             }
		                            }
	                            ]
                            )
                            global count_events
                            count_events = 3                          

            if (count_events == 3):
                event3 = list_events[2]

                client.chat_postMessage(
                    channel=channel_test,
                    blocks= [
		                {
			                "type": "section",
			                "text": {
			                	"type": "mrkdwn",
			                	"text": "Do you want to track *'"+event3+"'* in your timecard?"
			                 }
		                }
	                ]
                )
                
                @slack_event_adapter.on('message')
                def message2(payload):
                    event2 = payload.get('event', {})
                    channel_id2 = event2.get('channel')
                    user_id2 = event2.get('user')
                    text2 = event2.get('text')

                    # filters response to only use non-bot and only in test channel
                    if ((BOT_ID != user_id2) and (channel_id2 == channel_test_id)):
                
                        if (text2.lower() == 'yes'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "How many *minutes* do you want to track?"
			                             }
		                            }
	                            ]
                            )

                            @slack_event_adapter.on('message')
                            def message3(payload):
                                event3 = payload.get('event', {})
                                channel_id3 = event3.get('channel')
                                user_id3 = event3.get('user')
                                text3 = event3.get('text')

                                # filters response to only use non-bot and only in test channel
                                if ((BOT_ID != user_id3) and (channel_id3 == channel_test_id)):

                                   if (int(text3) > 0) and (int(text3) < 500):
                                        client.chat_postMessage(
                                            channel=channel_test,
                                            blocks= [
		                                        {
			                                        "type": "section",
			                                        "text": {
			                                        	"type": "mrkdwn",
			                                        	"text": "What *company* is this event for? (Reply with *'Done'* after you send this)\n\n_Is this event is non-billable, please enter *'Computacenter'*._"
			                                        }
		                                        }
	                                        ]
                                        )
                                        global count_events
                                        count_events = 2
            
                        if (text2.lower() == 'no'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "*Noted.* Reply *'Track'* to track another"
			                             }
		                            }
	                            ]
                            )
                            global count_events
                            count_events = 2  

            if (count_events == 2):
                event2 = list_events[1]

                client.chat_postMessage(
                    channel=channel_test,
                    blocks= [
		                {
			                "type": "section",
			                "text": {
			                	"type": "mrkdwn",
			                	"text": "Do you want to track *'"+event2+"'* in your timecard?"
			                 }
		                }
	                ]
                )
                
                @slack_event_adapter.on('message')
                def message2(payload):
                    event2 = payload.get('event', {})
                    channel_id2 = event2.get('channel')
                    user_id2 = event2.get('user')
                    text2 = event2.get('text')

                    # filters response to only use non-bot and only in test channel
                    if ((BOT_ID != user_id2) and (channel_id2 == channel_test_id)):
                
                        if (text2.lower() == 'yes'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "How many *minutes* do you want to track?"
			                             }
		                            }
	                            ]
                            )

                            @slack_event_adapter.on('message')
                            def message3(payload):
                                event3 = payload.get('event', {})
                                channel_id3 = event3.get('channel')
                                user_id3 = event3.get('user')
                                text3 = event3.get('text')

                                # filters response to only use non-bot and only in test channel
                                if ((BOT_ID != user_id3) and (channel_id3 == channel_test_id)):

                                   if (int(text3) > 0) and (int(text3) < 500):
                                        client.chat_postMessage(
                                            channel=channel_test,
                                            blocks= [
		                                        {
			                                        "type": "section",
			                                        "text": {
			                                        	"type": "mrkdwn",
			                                        	"text": "What *company* is this event for? (Reply with *'Done'* after you send this)\n\n_Is this event is non-billable, please enter *'Computacenter'*._"
			                                        }
		                                        }
	                                        ]
                                        )
                                        global count_events
                                        count_events = 1
            
                        if (text2.lower() == 'no'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "*Noted.* Reply *'Track'* to track another"
			                             }
		                            }
	                            ]
                            )
                            global count_events
                            count_events = 1  

            if (count_events == 1):
                event1 = list_events[0]

                client.chat_postMessage(
                    channel=channel_test,
                    blocks= [
		                {
			                "type": "section",
			                "text": {
			                	"type": "mrkdwn",
			                	"text": "Do you want to track *'"+event1+"'* in your timecard?"
			                 }
		                }
	                ]
                )
                
                @slack_event_adapter.on('message')
                def message2(payload):
                    event2 = payload.get('event', {})
                    channel_id2 = event2.get('channel')
                    user_id2 = event2.get('user')
                    text2 = event2.get('text')

                    # filters response to only use non-bot and only in test channel
                    if ((BOT_ID != user_id2) and (channel_id2 == channel_test_id)):
                
                        if (text2.lower() == 'yes'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "How many *minutes* do you want to track?"
			                             }
		                            }
	                            ]
                            )

                            @slack_event_adapter.on('message')
                            def message3(payload):
                                event3 = payload.get('event', {})
                                channel_id3 = event3.get('channel')
                                user_id3 = event3.get('user')
                                text3 = event3.get('text')

                                # filters response to only use non-bot and only in test channel
                                if ((BOT_ID != user_id3) and (channel_id3 == channel_test_id)):

                                   if (int(text3) > 0) and (int(text3) < 500):
                                        client.chat_postMessage(
                                            channel=channel_test,
                                            blocks= [
		                                        {
			                                        "type": "section",
			                                        "text": {
			                                        	"type": "mrkdwn",
			                                        	"text": "What *company* is this event for? (Reply with *'Done'* after you send this)\n\n_Is this event is non-billable, please enter *'Computacenter'*._"
			                                        }
		                                        }
	                                        ]
                                        )
                                        global count_events
                                        count_events = 0
            
                        if (text2.lower() == 'no'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "*Noted.* Reply *'Track'* to track another"
			                             }
		                            }
	                            ]
                            )
                            global count_events
                            count_events = 0  

            if (count_events == 0):
                event_1 = list_events[-1]

                client.chat_postMessage(
                    channel=channel_test,
                    blocks= [
		                {
			                "type": "section",
			                "text": {
			                	"type": "mrkdwn",
			                	"text": "Do you want to track *'"+event_1+"'* in your timecard?"
			                 }
		                }
	                ]
                )
                
                @slack_event_adapter.on('message')
                def message2(payload):
                    event2 = payload.get('event', {})
                    channel_id2 = event2.get('channel')
                    user_id2 = event2.get('user')
                    text2 = event2.get('text')

                    # filters response to only use non-bot and only in test channel
                    if ((BOT_ID != user_id2) and (channel_id2 == channel_test_id)):
                
                        if (text2.lower() == 'yes'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "How many *minutes* do you want to track?"
			                             }
		                            }
	                            ]
                            )

                            @slack_event_adapter.on('message')
                            def message3(payload):
                                event3 = payload.get('event', {})
                                channel_id3 = event3.get('channel')
                                user_id3 = event3.get('user')
                                text3 = event3.get('text')

                                # filters response to only use non-bot and only in test channel
                                if ((BOT_ID != user_id3) and (channel_id3 == channel_test_id)):

                                   if (int(text3) > 0) and (int(text3) < 500):
                                        client.chat_postMessage(
                                            channel=channel_test,
                                            blocks= [
		                                        {
			                                        "type": "section",
			                                        "text": {
			                                        	"type": "mrkdwn",
			                                        	"text": "What *company* is this event for? (Reply with *'Done'* after you send this)\n\n_Is this event is non-billable, please enter *'Computacenter'*._"
			                                        }
		                                        }
	                                        ]
                                        )
                                        global count_events
                                        count_events = -1
            
                        if (text2.lower() == 'no'):
                            client.chat_postMessage(
                                channel=channel_test,
                                blocks= [
		                            {
			                            "type": "section",
			                            "text": {
			                            	"type": "mrkdwn",
			                            	"text": "*Noted.* Reply *'Track'* to track another"
			                             }
		                            }
	                            ]
                            )
                            global count_events
                            count_events = -1  

    # DO YOU WANT TO TRACK TIME - NO
        # user responds they dont want to track time
        if (text.lower() == 'bye'):
            client.chat_postMessage(
                channel=channel_test,
                text='Rude. Thanks anyway. Have a great day. Boti out!'
            )
               
    # INPUT NOT RECOGNIZED, ERROR
        if (text.lower() == 'oops'):
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

    # EXTRA
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

        if (text.lower() == 'fund me'):
            client.chat_postMessage(
                channel=channel_test,
                blocks= [
	            	{
		                "type": "image",
		                "image_url": "https://www.investopedia.com/thmb/lqOcGlE7PI6vLMzhn5EDdO0HvYk=/1337x1003/smart/filters:no_upscale()/GettyImages-1054017850-7ef42af7b8044d7a86cfb2bff8641e1d.jpg",
		                "alt_text": "inspiration"
	                }
                ]
            )

        if (text.lower() == 'rich'):
            client.chat_postMessage(
                channel=channel_test,
                blocks= [
	            	{
		                "type": "image",
    	                "image_url": "https://pbs.twimg.com/profile_images/1074378429468995586/gb9sOv1s.jpg",
		                "alt_text": "inspiration"
	                }
                ]
            )

        if (text.lower() == 'tell me a joke'):
            image=random.randint(1,5)

            if (image == 1):
                client.chat_postMessage(
                    channel=channel_test,
                    blocks= [
		        	    {
		                    "type": "image",
		                    "image_url": "https://www.rd.com/wp-content/uploads/2019/03/101jokes9.jpg",
		                    "alt_text": "inspiration"
		                }
	                ]
                )                
            if (image == 2):
                client.chat_postMessage(
                    channel=channel_test,
                    blocks= [
		        	    {
		                    "type": "image",
		                    "image_url": "https://www.rd.com/wp-content/uploads/2018/09/69-Short-Jokes-Anyone-Can-Remember-nicole-fornabaio-rd.com_.jpg",
		                    "alt_text": "inspiration"
		                }
	                ]
                )                
            if (image == 3):
                client.chat_postMessage(
                    channel=channel_test,
                    blocks= [
		        	    {
		                    "type": "image",
		                    "image_url": "https://www.rd.com/wp-content/uploads/2018/09/62-Short-Jokes-Anyone-Can-Remember-nicole-fornabaio-rd.com_.jpg",
		                    "alt_text": "inspiration"
		                }
	                ]
                )                
            if (image == 4):
                client.chat_postMessage(
                    channel=channel_test,
                    blocks= [
		        	    {
		                    "type": "image",
		                    "image_url": "https://www.rd.com/wp-content/uploads/2019/03/101jokes5.jpg",
		                    "alt_text": "inspiration"
		                }
	                ]
                )                
            if (image == 5):
                client.chat_postMessage(
                    channel=channel_test,
                    blocks= [
		     	        {
	                        "type": "image",
		                    "image_url": "https://www.rd.com/wp-content/uploads/2019/03/101jokes7.jpg",
		                    "alt_text": "inspiration"
		                }
	                ]
                )


# debugger which coincidently causes messages to send twice, will not work without it though
if __name__ == "__main__":
    	app.run(debug=True)
