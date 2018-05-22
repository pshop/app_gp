from flask import render_template, jsonify, request
from app import app
from app import parser
from app import request_google_api as google
from app import request_wiki_api as wiki
from config import ConfigGrandpy as grandpy
import sys
import random

@app.route('/')
def index():
    return render_template('index.html')
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():
    didnt_understant = 0
    question = request.form['question']
    p = parser.Parser(question)
    g = google.RequestGoogleApi(p.parsed_string)
    w = wiki.RequestWikiApi(g.search_term)


    if g.adress:
        data = {
            "question": question,
            "response1": g.adress,
            "response2": w.wiki_sum
        }
        didnt_understant = 0
        return jsonify(data)
    else:
        data = {
            "question": question,
            "response1": random.choice(grandpy.missunderstood1),
            "response2": ''
        }
        didnt_understant += 1
    
    
if __name__ == "__main__":
    app.run(debug = True)