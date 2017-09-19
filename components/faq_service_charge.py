# -*- coding: utf-8 -*-
import requests
import json
from meya import Component


class faq_service_charge(Component):

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
                msg = self.create_message(text='We charge a 15% service fee on the interests that are earned by investors. The service fee will only be deducted if you receive interests payments.')
            elif(user_type=='borrower'):
                msg = self.create_message(text='There are no fees for loan application, and approval. We only charge a competitive fee (of between 2% to 5%), upon successful disbursement of your loan.')
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