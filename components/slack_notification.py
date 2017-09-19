# -*- coding: utf-8 -*-
import requests
import json
from meya import Component


class slack_notification(Component):

    def start(self):
        #bot test channel
        #slack_url = "https://hooks.slack.com/services/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"
        
        #sg-sales-marketing channel
        slack_url = "https://hooks.slack.com/services/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"
        name = self.db.flow.get('name')
        company_name = self.db.flow.get('company_name')
        loan_amount = self.db.flow.get('loan_amount')
        phone_no = self.db.flow.get('phone_no')
        email = self.db.flow.get('email')
        payload = {'text': "There is a new user eligible to apply for a loan; Name: %s, Company Name: %s, Loan Amount: %s, Contact Number: %s, Email: %s" % (name, company_name, loan_amount, phone_no, email)}
        res = requests.post(slack_url, data=json.dumps(payload))
        print(res.text)
        return self.respond(message=None, action="next")