# -*- coding: utf-8 -*-
import requests
import json
from meya import Component


class user_check(Component):

    def start(self):
        email = self.db.user.get('email')
        if email!="":
            msg = "user_msg"
        else:
            msg = "lead_msg"
        
        return self.respond(message=msg, action="next")
        
        
            
    
