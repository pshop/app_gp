from flask import render_template, jsonify, request
from app import app
from app import AskGrandpy as ag

@app.route('/')
def index():
    return render_template('index.html')
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():

    question = request.form['question']
    answers = ag.AskGrandpy(question)
    data = {}
    answers.get_answer()
    
    data["question"] = question
    data["response1"] = answers.address
    data["response2"] = answers.wiki

    if answers.error :
        data["image"] = "https://pbs.twimg.com/profile_images/587949417577066499/3uCD4xxY_400x400.jpg"
    else :
        data["image"] = f"https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyCPcXSPzlsfowlu0SmioWA8oSVEC5hjTaM&center={answers.address}&zoom=15&size=600x400&markers={answers.address}&format=jpg"

    return jsonify(data)
    
if __name__ == "__main__":
    app.run(debug = True)