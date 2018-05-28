# -*-coding:utf-8 -*
from app.parser import Parser
from app.request_wiki_api import RequestWikiApi
from app.request_google_api import RequestGoogleApi
from app.ask_grandpy import AskGrandpy

def test_parser():
    my_parser = Parser("quelle est l'adresse de la poste la plus proche ?")
    assert my_parser.parsed_string == "poste"
    my_parser = Parser("salut grandpy comment ça va ? Tu sais ou est la tour eiffel par hasard ?")
    assert my_parser.parsed_string == "tour eiffel"
    my_parser = Parser("Hello quelle est l'adresse de openclassroom stp?")
    assert my_parser.parsed_string == "openclassroom"
    my_parser = Parser("")
    assert my_parser.parsed_string == ""
    my_parser = Parser(22)
    assert my_parser.parsed_string == ""


def test_wiki():
    wiki = RequestWikiApi("requète")
    assert  wiki.request == "requète"
    assert type(wiki.request) is str

def test_google():
    g = RequestGoogleApi("test")
    assert g.question == "test"
    assert g.adress == None
    assert g.search == None
    assert type(g.question) is str

def test_ask_gp():
    ag = AskGrandpy("test")
    assert ag.question == "test"
    assert type(ag.question) is str
    assert ag.address == ''
    assert ag.wiki == ''
    assert ag.error == False