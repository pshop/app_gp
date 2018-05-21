from flask import (Flask, request, jsonify, render_template)
                   
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
        
        
@app.route('/ajax', methods = ['POST'])
def ajax_request():
    q = request.form['question']
    data = {
        "question": q,
        "response": "Salut c'est cool"
    }
    return jsonify(data)
    
    
if __name__ == "__main__":
    app.run(debug = True)