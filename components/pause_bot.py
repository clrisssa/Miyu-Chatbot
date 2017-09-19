import requests
from requests.auth import HTTPBasicAuth
from meya import Component

class pause_bot(Component):
    def start(self):


        api_key = "cmqus8hgeXdbVqjmi93FyCMjCU31czKK"
        user_id = self.db.flow.get('user_id')
        print("USER_ID: %s" % user_id)
        url = "https://api.meya.ai/pause"
        data = {
            "user_id": user_id,
            "integration": "intercom",
            "cancel_flows": True
        }
        
        auth = HTTPBasicAuth(api_key, None)
        
        res = requests.post(url, json=data, auth=auth)
        data = res.json()
        print("DATA: %s" % data)
        return self.respond(message=None, action="next")