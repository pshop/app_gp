import json
import requests
from config import ConfigGoogle as CG
import sys
from app import request_google_api as g
from app import request_wiki_api as w

def test_google():
    req = [
    # g.RequestGoogleApi('poste'),
    # g.RequestGoogleApi('louvre'),
    # g.RequestGoogleApi('openclassrooms'),
    # g.RequestGoogleApi('tour eiffel'),
    # g.RequestGoogleApi('apple store'),
    # g.RequestGoogleApi('saveurs couleurs'),
    g.RequestGoogleApi('eiwufiweh')
    ]
    for r in req:
        
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        r.req()
        wiki = w.RequestWikiApi(r.search)
        print(r.adress)
        print('- - - - - - - - - - - - - - - - - - ')
        print(r.search)
        print('- - - - - - - - - - - - - - - - - - ')
        print(wiki.summary_extr)

        

if __name__ == '__main__':
    test_google()