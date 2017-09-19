# -*- coding: utf-8 -*-
import requests
import json
from meya import Component
from dateutil import relativedelta as rdelta
from datetime import date
import datetime


class count_years(Component):

    def start(self):
        params = self.db.flow.get('parameters')
        duration = params['duration']

        year_since = int(params['date-time'][:4])
        if(duration):
            period = duration['amount']
            unit = duration['unit']
            print("DURATIONNNNN****: ")
            print(amount)
        
        if(year_since):
            print("YEARRR****: ")
            print(year_since)
            current_year = int(datetime.datetime.now().year)
            print("CURRENTTT****: ")
            print(current_year)
            period = current_year - year_since
            print("HOW LONG?****: ")
            print(period)
        if (period):
            if period>1:
                action = "state5"
                return self.respond(message=None, action="next")
            else:
                action = "ambiguous_state4"
    