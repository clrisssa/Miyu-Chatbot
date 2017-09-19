# -*- coding: utf-8 -*-
from meya import Component
from meya.cards import Image
from meya.cards import Card
import requests

API_KEY = "ea993488463f4349ba0d0c7448dc9633"
API_URL = "http://api.giphy.com/v1/gifs/{image_id}?api_key={key}"

class GiphyById(Component):
    """Outputs a random giphy url based on passed in tag as either
    a property or flow db"""

    def start(self):
        print("START")
        # read in the gif type from the flow datastore
        # learn more: http://docs.meya.ai/docs/database-overview
        # tag = self.db.flow.get('tag') or "funny"
        image_id = self.db.flow.get('image_id')
        text = self.db.flow.get('text')
        print("IMAGE_ID: %s" % image_id)

        # use the requests package to make an API call to giphy
        response = requests.get(API_URL.format(image_id=image_id, key=API_KEY))
        print("RES: %s" % response.text)
        image_url = response.json()['data']['images']['fixed_height']['url']
        print("IMAGE_URL: %s" % image_url)

        # create an image card and create the corresponding message
        image_card = Image(image_url=image_url)
        card = Card(text=text, image_url=image_url)
        # message = self.create_message(card=image_card)
        message = self.create_message(card=card)
        # respond with the message and "next" action
        return self.respond(message=message, action="next")
