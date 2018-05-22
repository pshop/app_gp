import json
import requests
from config import ConfigGoogle as CG
import sys

class RequestGoogleApi:

    def __init__(self, question):
        CG.GOOGLE_API_ARGS['query'] = question
        self.r = requests.get(CG.GOOGLE_API_BASE_URL, params= CG.GOOGLE_API_ARGS)
        self.r = self.r.json()

    @property
    def adress(self):
        try:
            adr = self.r['results'][0]['formatted_address']
        except IndexError:
            return False
        return adr

    @property
    def search_term(self):
        try:
            s_t = self.r['results'][0]['name']
        except IndexError:
            return False
        return s_t