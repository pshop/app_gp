from app import request_google_api as g
from app import request_wiki_api as w
from app import parser as p
from config import ConfigGrandpy
import random

class AskGrandpy:
    
    def __init__(self, question):
        self.question = str(question)
        self.address = ''
        self.wiki = ''
        self.error = False

    def get_answer(self):
        
        google = g.RequestGoogleApi(p.Parser(self.question).parsed_string)
        google.req()
        if google.search and google.adress:
            self.address = f"{random.choice(ConfigGrandpy.intro_address)}{google.adress}."
            self.wiki = self.get_wiki(google.search)
            self.error = False
        else:
            self.address = random.choice(ConfigGrandpy.missunderstood)
            self.wiki = 'tactical dot => .'
            self.error = True

    def get_wiki(self, search):
        wiki = w.RequestWikiApi(search)

        if wiki.summary_extr:
            return f"{random.choice(ConfigGrandpy.intro_wiki)}{wiki.summary_extr}"
        else:
            return random.choice(ConfigGrandpy.wiki_no_result)

    