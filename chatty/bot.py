 # Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount


class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):
        if turn_context.activity.text == "Hi" or turn_context.activity.text == "hi":
            await turn_context.send_activity("Hello I am bot how can i help you.")

        if turn_context.activity.text == "tell me about yourself":
            await turn_context.send_activity("I am a bot and my name is Chatty.")
        
        if turn_context.activity.text == "how is your health":
            await turn_context.send_activity("I'm a computer program, so I'm always healthy")
        
        if turn_context.activity.text == "favourite game":
            await turn_context.send_activity("I'm a very big fan of Taekwondo")
        
        if turn_context.activity.text == "favourite sportsman":
            await turn_context.send_activity("Aaron cock")
        
        if turn_context.activity.text == "what is your age":
            await turn_context.send_activity("I'm a computer program dude\nSeriously you are asking me this?")
        
        if turn_context.activity.text == "what you want":
            await turn_context.send_activity("Make me an offer I can't refuse")
        
        if turn_context.activity.text == "quit":
            await turn_context.send_activity("BBye take care. See you soon :) ","It was nice talking to you.")
            quit()
    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
