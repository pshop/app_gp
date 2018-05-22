#! /usr/bin/env python3
# coding: utf-8
import re
from config import ConfigParser

class Parser:
    def __init__(self, string_to_parse):
        self.string_to_parse = string_to_parse
        self.final_answer = str()

    @property
    def parsed_string(self):
        raw_list = self.__string_to_list(self.string_to_parse)
        cleaned_list = self.__delete_irrelevant_words(raw_list)
        return self.__list_to_string(cleaned_list)

    def __string_to_list(self, my_string):
        """
        Get the string send by the user and split the words in a list.
        """
        my_string = my_string.lower()
        my_string = re.sub("[^a-zéèê\\s]", " ", my_string)
        my_list = my_string.split(' ')
        my_list = [word for word in my_list if word != '']
        return my_list

    def __delete_irrelevant_words(self, my_list):
        my_list = [word for word in my_list if word not in ConfigParser.STOP_WORDS]
        return my_list

    def __list_to_string(self, my_list):
        return " ".join(my_list)


if __name__ == "__main__":
    test = Parser("quelle est l'adresse de la poste la plus proche ?")
    print(test.parsed_string)