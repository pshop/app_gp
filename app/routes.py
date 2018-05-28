from flask import render_template, jsonify, request
from app import app
from app import ask_grandpy as ag
from app import parser as p
import sys

@app.route('/')
def index():
    return render_template('index.html')
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():

    question = request.form['question']
    answers = ag.AskGrandpy(question)
    data = {}
    raw_address = answers.get_answer()
    
    data["question"] = question
    data["response1"] = answers.address
    print(answers.address, file =  sys.stdout)
    data["response2"] = answers.wiki

    if answers.error :
        data["image"] = "https://pbs.twimg.com/profile_images/587949417577066499/3uCD4xxY_400x400.jpg"
    else :
        data["image"] = f"https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyCPcXSPzlsfowlu0SmioWA8oSVEC5hjTaM&center={raw_address}&zoom=15&size=600x400&markers={raw_address}&format=jpg"

    return jsonify(data)
    
if __name__ == "__main__":
    app.run(debug = True)