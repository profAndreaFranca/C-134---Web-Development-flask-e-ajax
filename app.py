from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *


app = Flask(__name__)

@app.route("/hello")
def firs_flask():
    return "Hello World!"

@app.route("/flask")
def second_flask():
    return "Hello Flask"

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Obtenha a entrada de texto do requisição POST 
    input_text = request.json.get("text")
    
    if not input_text:
        response = {
            "status": "error",
            "message": "O texto precisa ser digitado"
        }
        return jsonify(response)
        # Resposta a enviar se o input_text for indefinido
    else:
        predicted_emotion,predicted_emoji = predict(input_text)
    
        # Resposta a enviar se o input_text não for indefinido
        response = {
            "status": "success",
            "data": {
                "predicted_emotion": predicted_emotion,
                "predicted_emoji": predicted_emoji     
                }
        }
        # Enviar resposta   
        return jsonify(response)      
        
       
app.run(debug=True)



    