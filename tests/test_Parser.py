# -*-coding:utf-8 -*
from app.parser import *

def test_parser():
    my_parser = Parser("Salut GrandpyBot, tu vas bien ? Connais tu la rue de la servette à genève ?")
    assert my_parser.parsed_string == "rue servette genève"
    my_parser = Parser("Où est la tour Eiffel ?")
    assert my_parser.parsed_string == "tour eiffel"
