# -*-coding:utf-8 -*
from app.parser import *

def test_parser():
    my_parser = Parser("quelle est l'adresse de la poste la plus proche ?")
    assert my_parser.parsed_string == "poste"
    my_parser = Parser("salut grandpy comment ça va ? Tu sais ou est la tour eiffel par hasard ?")
    assert my_parser.parsed_string == "tour eiffel"
    my_parser = Parser("Hello quelle est l'adresse de openclassroom stp?")
    assert my_parser.parsed_string == "openclassroom"
