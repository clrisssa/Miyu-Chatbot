# -*- coding: utf-8 -*-
import requests
import json
from meya import Component


class faq_tax(Component):

    def start(self):
        params = self.db.flow.get('parameters')
        tax_resident = params['tax_resident']
        print("TAX RESIDENT: ")
        print(params['tax_resident'])

        if (tax_resident):
            print("IF")
            if(tax_resident=='is_tax_resident'):
                self.db.flow.set('is_tax_resident', str('true'))

            elif(tax_resident=='not_tax_resident'):
                self.db.flow.set('is_tax_resident', str('false'))

        
        return self.respond(message=None, action="next")