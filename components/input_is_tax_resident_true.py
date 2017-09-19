# -*- coding: utf-8 -*-
import requests
import json
from meya import Component


class input_is_tax_resident_true(Component):

    def start(self):
        self.db.flow.set('is_tax_resident', str('true'))
        return self.respond(message=None, action="next")