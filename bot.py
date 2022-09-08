import slack_sdk
from flask import Flask
from slackeventsapi import SlackEventAdapter
from os import environ as env
from dotenv import load_dotenv
load_dotenv()

print(format(env['SIGNING_SECRET']))

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(env['SIGNING_SECRET'], '/slack/events', app)

client = slack_sdk.WebClient(token=env['SLACK_TOKEN'])

@ slack_event_adapter.on('message')
def message(payload):
    print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if text == "hi":
        client.chat_postMessage(channel=channel_id,text="Hello")

if __name__ == "__main__":
    app.run(debug=True)
