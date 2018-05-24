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

    question = request.form['question']
    p = parser.Parser(question)
    g = google.RequestGoogleApi(p.parsed_string)
    w = wiki.RequestWikiApi(g.search)


    
    data = {
        "question": question,
        "response1": "adresse",
        "response2": "résumé wikipedia"
    }
    return jsonify(data)
    
    
if __name__ == "__main__":
    app.run(debug = True)