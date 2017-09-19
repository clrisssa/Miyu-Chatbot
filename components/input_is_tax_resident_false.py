# -*- coding: utf-8 -*-
import requests
import json
from meya import Component


class input_is_tax_resident_false(Component):

    def start(self):
        self.db.flow.set('is_tax_resident', str('false'))
        return self.respond(message=None, action="next")