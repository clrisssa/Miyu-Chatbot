# -*- coding: utf-8 -*-
import datetime
from datetime import time
from datetime import timedelta
from meya import Component


class CheckIfOpen(Component):

    def start(self):
        today = datetime.datetime.today() + timedelta(hours=8)
        dow = today.weekday()
        current_time = today.time()
        start_open_time = datetime.time(9,0)
        start_close_time = datetime.time(18,0)
        print ("TIME %s" % current_time)
        print ("OPEN TIME %s"% start_open_time)
        print ("CLOSE TIME %s"% start_close_time)

        ooi = (current_time < start_open_time or current_time > start_close_time)
        yoo = current_time > start_close_time
        print("BOOlean %s" % ooi)
        # print("BOOlean2 %s" % yoo)

        if dow in (5, 6) or (current_time < start_open_time or current_time > start_close_time):
            action = "is_closed"
            print("CLOSED")
        else:
            action = "is_open"
            print("OPEN")
        return self.respond(action=action)
