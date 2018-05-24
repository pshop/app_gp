import json
import requests
from config import ConfigGoogle as CG
import sys
from app import request_google_api as g
from app import request_wiki_api as w
from app import AskGrandpy as ag

def test_google():
    req = [
    g.RequestGoogleApi('poste'),
    g.RequestGoogleApi('louvre'),
    g.RequestGoogleApi('openclassrooms'),
    g.RequestGoogleApi('tour eiffel'),
    g.RequestGoogleApi('apple store'),
    g.RequestGoogleApi('saveurs couleurs'),
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

def test_askgp():
    req = [
    ag.AskGrandpy('poste'),
    ag.AskGrandpy('louvre'),
    ag.AskGrandpy('openclassrooms'),
    ag.AskGrandpy('tour eiffel'),
    ag.AskGrandpy('apple store'),
    ag.AskGrandpy('saveurs couleurs'),
    ag.AskGrandpy('eiwufiweh')
    ]

    for r in req:
        r.get_answer()
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(f"question : {r.question}")
        print(f"adresse : {r.address}")
        print(f"wiki : {r.wiki}")

        

if __name__ == '__main__':
    #test_google()
    test_askgp()