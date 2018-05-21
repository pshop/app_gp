from flask import render_template, jsonify, request
from app import app
from app import parser
from app import request_google_api as rga
import sys

@app.route('/')
def index():
    return render_template('index.html')
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():

    question = request.form['question']
    p = parser.Parser(question)
    g = rga.RequestGoogleApi(p.parsed_string)

    data = {
        "question": question,
        "response": g.adress
    }
    return jsonify(data)
    
    
if __name__ == "__main__":
    app.run(debug = True)