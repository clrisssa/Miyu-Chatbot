# -*- coding: utf-8 -*-
import requests
import json
from meya import Component


class href(Component):

    def start(self):
        msg = self.create_message(text='<a href="http://www.yahoo.com">here</a>')

        
        return self.respond(message=msg, action="next")
        
        
            
    
