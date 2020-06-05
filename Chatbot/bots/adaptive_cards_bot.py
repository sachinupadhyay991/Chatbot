# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import os
import random

from botbuilder.core import ActivityHandler, TurnContext, CardFactory
from botbuilder.schema import ChannelAccount, Attachment, Activity, ActivityTypes

CARDS = [
    "resources/FlightItineraryCard.json"
]


class AdaptiveCardsBot(ActivityHandler):
    a={"Jaipur":"JPR","Goa":"G","Usa":"USA","Germany":"GER","Pune":"PU","J&k":"J"}
    name=[]
    source=[]
    destination=[]
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    f"Welcome to Adaptive Cards Bot  {member.name}. This bot will "
                    f"introduce you to Adaptive Cards. Type anything to see an Adaptive "
                    f"Card."
                )
    
    async def on_message_activity(self, turn_context: TurnContext):
        
        if turn_context.activity.text.title() in ["Hi","Hello","Hey","Hy"]:
            await turn_context.send_activity("Hello , Enter the Name.")
        
        elif turn_context.activity.text.title() not in AdaptiveCardsBot.a and len(AdaptiveCardsBot.source) == 0 :
            await turn_context.send_activity("Enter the Source.")
            AdaptiveCardsBot.name.append(turn_context.activity.text)
            

        elif turn_context.activity.text.title() in AdaptiveCardsBot.a and len(AdaptiveCardsBot.source) == 0:
            await turn_context.send_activity("Enter the Destination.")
            AdaptiveCardsBot.source.append(turn_context.activity.text)
            

        elif turn_context.activity.text.title() in AdaptiveCardsBot.a:
            AdaptiveCardsBot.destination.append(turn_context.activity.text)
            await turn_context.send_activity("Enter Fd to view your flight details.")
        
        elif turn_context.activity.text.title() == "Fd":
            message = Activity(
                text="Here is an Adaptive Card:",
                type=ActivityTypes.message,
                attachments=[self._create_adaptive_card_attachment()],
            )

            await turn_context.send_activity(message)

    def _create_adaptive_card_attachment(self) -> Attachment:        
        card_path = os.path.join(os.getcwd(), CARDS[0])
        with open(card_path, "r") as in_file:
            card_data = json.load(in_file)

        card_data["body"][1]["text"]=AdaptiveCardsBot.name[0]
        card_data["body"][4]["columns"][0]["items"][0]["text"]=AdaptiveCardsBot.source[0].title()
        card_data["body"][4]["columns"][2]["items"][0]["text"]=AdaptiveCardsBot.destination[0].title()
        card_data["body"][7]["columns"][0]["items"][0]["text"]=AdaptiveCardsBot.destination[0].title()
        card_data["body"][7]["columns"][2]["items"][0]["text"]=AdaptiveCardsBot.source[0].title()
        card_data["body"][4]["columns"][0]["items"][1]["text"]=AdaptiveCardsBot.a[AdaptiveCardsBot.source[0].title()]
        card_data["body"][4]["columns"][2]["items"][1]["text"]=AdaptiveCardsBot.a[AdaptiveCardsBot.destination[0].title()]
        card_data["body"][7]["columns"][0]["items"][1]["text"]=AdaptiveCardsBot.a[AdaptiveCardsBot.destination[0].title()]
        card_data["body"][7]["columns"][2]["items"][1]["text"]=AdaptiveCardsBot.a[AdaptiveCardsBot.source[0].title()]
        with open(card_path, "w") as in_file:
            json.dump(card_data,in_file)

        return CardFactory.adaptive_card(card_data)
