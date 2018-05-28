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


mock_loc = {
    "location": {
        "lat": 666,
        "lng": 999
    }
}

mock_req_place = {
    'status' :'OVER_QUERY_LIMIT',
    'results':[
        {
            'formatted_address': 'Adresse Test',
            'name': 'Nom test'
        }
    ]
}

mock_req_place_nearby = {
    'status' :'OK',
    'results':[
        {
            'vicinity': "Adresse TEST"
        }
    ]
}

mock_req_autocomp_place = {
    'status' :'OK',
    'predictions':[
        {
            'description' : "description test"
        }
    ],
    'results':[
        {
            'formatted_address' : 'test adresse formatée'
        }
    ]
}

def test_google():
    # test __init__ RequestGoogleApi
    g = RequestGoogleApi("test")
    assert g.question == "test"
    assert g.adress == None
    assert g.search == None
    assert type(g.question) is str

    # test RequestGoogleApi.get_loc()
    assert g.get_loc(mock_loc) == "666,999"

    # test RequestGoogleApi.req_autocomp_place()
    test_auto_c = g.req_autocomp_place(mock_loc)
    assert test_auto_c['input'] == "test"
    assert test_auto_c['location'] == mock_loc

    # test RequestGoogleApi.req_place_nearby()
    test_place_nb = g.req_place_nearby(mock_loc)
    assert test_place_nb['location'] == mock_loc
    assert test_place_nb['keyword'] == "test"

    # test RequestGoogleApi.req_place()
    assert g.req_place(True) == "test"

    # test RequestGoogleApi.req()
    g.req(mock_req_place)
    assert g.adress == 'Trop de questions pour aujourd\'hui'
    assert g.search == 'Je suis épuisé.'

    mock_req_place['status'] = 'OK'
    g.req(mock_req_place)
    assert g.adress == 'Adresse Test'
    assert g.search == 'Nom test'

    mock_req_place['status'] = 'test'
    g.req(mock_req_place, mock_req_place_nearby)
    assert g.adress == "Adresse TEST"
    assert g.search == "test"

    mock_req_place_nearby['status'] = 'test'
    g.req(mock_req_place, mock_req_place_nearby, mock_req_autocomp_place)
    assert g.question == "description test"


def test_ask_gp():
    ag = AskGrandpy("test")
    assert ag.question == "test"
    assert type(ag.question) is str
    assert ag.address == ''
    assert ag.wiki == ''
    assert ag.error == False