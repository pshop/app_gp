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
    answers.get_answer()
    
    data = {
        "question": question,
        "response1": answers.address,
        "response2": answers.wiki
    }
    return jsonify(data)
    
    
if __name__ == "__main__":
    app.run(debug = True)