# -*- coding: utf-8 -*-
import requests
import json
from meya import Component


class faq_interest_rates(Component):

    def start(self):
        params = self.db.flow.get('parameters')
        user_type = params['user_type']
        print("USER_TYPE: ")
        print(params['user_type'])
        # fulfillment = self.db.flow.get('fulfillment')
        # spch = fulfillment['speech']
        #print("SPEECH: ")
        #print(spch)

        
        msg = ""
        if (user_type):
            print("IF")
            if(user_type=='investor'):
                msg = self.create_message(text='Interest rates are between 9% to 14%. As per most investments, higher rewards come with higher risk. We assign higher interest rates for the latter SMEs to compensate for the higher risks investors assume.')
            elif(user_type=='borrower'):
                msg = self.create_message(text='On average, interest rates range from 9% to 14% per annum on a simple interest basis. Our interest rates are determined by our risk-based pricing model which is derived through our proprietary credit scoring system.')
        else:
            # print("ELSE")
            # spch = fulfillment['speech']
            self.db.flow.set('reply', str('exists'))

            # if(spch):
            msg = self.create_message(text='Are you asking as an investor or borrower?')
            # else:
            #     msg = None
            # print("FULFILLMENT: ")
            # print(fulfillment)
        
        return self.respond(message=msg, action="next")