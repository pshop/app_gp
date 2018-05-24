import json
import requests
from config import ConfigGoogle as CG
import sys


class RequestGoogleApi:

    def __init__(self, question):
        self.question = question
        self.adress = None
        self.search = None


    def req_place(self):
        """
        Makes a basic search on google map, work for stecific searches like 'tour eiffel'
        'le louvre' but not for generic ones like 'post office'
        """

        CG.PLACES_API_ARGS['query'] = self.question
        r = requests.get(CG.PLACES_API_BASE_URL, params= CG.PLACES_API_ARGS)
        return r.json()


    def req_place_nearby(self):
        """
        Makes a search on google map and will return the nearest place, works for generic searches
        """

        loc = self.get_loc()
        if loc :
            CG.PLACES_NEAR_API_ARGS["location"] = loc
            CG.PLACES_NEAR_API_ARGS["keyword"] = self.question
            r = requests.post(CG.PLACES_NEAR_BASE_URL, params=CG.PLACES_NEAR_API_ARGS)
            return r.json()
        else:
            return "La localisationd de l'appareil à échoué"


    def req_autocomp_place(self):

        CG.AUTOCOMP_API_ARGS['input'] = self.question
        location = self.get_loc()

        if location:
            CG.AUTOCOMP_API_ARGS['location'] = location
        else :
            del CG.AUTOCOMP_API_ARGS['location']

        r = requests.post(CG.AUTOCOMP_BASE_URL, params= CG.AUTOCOMP_API_ARGS)

        return r.json()


    def get_loc(self):
        """
        get localisation of the device
        """
        try:
            r = requests.post(CG.LOCATE_API_BASE_URL, params=CG.LOCATE_API_KEY).json()
        except:
            return None

        try: 
            lat = r['location']['lat']
            lng = r['location']['lng']
        except:
            return None
        
        return f"{str(lat)},{str(lng)}"
         

    def req(self):

        req = self.req_place()

        if req['status'] == 'OVER_QUERY_LIMIT':
            self.adress = 'Trop de questions pour aujourd\'hui'
            self.search = 'Je suis épuisé.'

        if req['status'] == 'OK':
            """ req_place() SUCCEED """
            self.adress  = req['results'][0]['formatted_address']
            self.search = req['results'][0]['name']

        else:
            """ req_place() FAILED """
            req = self.req_place_nearby()

            if req['status'] == 'OK':
                """ req_place_nearby() SUCCEED """
                self.adress = req["results"][0]['vicinity']
                self.search = self.question
                
            else:
                """ req_place_nearby() FAILED """
                req = self.req_autocomp_place()

                if req['status'] == 'OK':
                    self.question = req['predictions'][0]['description']
                    req = self.req_place()

                    if req['status'] == 'OK':
                        self.adress = req['results'][0]['formatted_address']
                        self.search = self.question

                    else:
                        return None
                
                else :
                    return None


        
