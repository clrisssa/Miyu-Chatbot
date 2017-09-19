# -*- coding: utf-8 -*-
import requests
import json
from meya import Component


class remove_flow_reply_data(Component):

    def start(self):
        self.db.flow.set('reply', None)
        user_type = None
        
        return self.respond(message=None, action="next")