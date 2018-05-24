from app import request_google_api as g
from app import request_wiki_api as w
from config import ConfigGrandpy
import random

class AskGrandpy:
    
    def __init__(self, question):
        self.question = question
        self.address = ''
        self.wiki = ''

    def get_answer(self):
        google = g.RequestGoogleApi(self.question)
        google.req()
        if google.search and google.adress:
            self.address = google.adress
            self.wiki = self.get_wiki(google.search)
        else:
            self.address = random.choice(ConfigGrandpy.missunderstood)

    def get_wiki(self, search):
        wiki = w.RequestWikiApi(search)

        if wiki.summary_extr:
            return wiki.summary_extr
        else:
            return random.choice(ConfigGrandpy.wiki_no_result)

    