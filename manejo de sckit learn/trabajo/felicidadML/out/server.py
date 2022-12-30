import joblib
import numpy as np 

from flask import Flask 
from flask import jsonify 

app = Flask(__name__)

#POST PARA PRUEBAS
@app.route('/predict', methods=['GET'])
def prediction():
    X_text = np.array([6.690085086,6.507914868,1.185295463,1.440451145,0.695137084,0.494519204,0.109457061,0.059739888,2.614005327])
    predict = model.predict(X_text.reshape(1,-1))
    return jsonify({'prediccion ': list(predict)})
m:
    
    model = joblib.load('../models/best_model.pkl')
    app.run(port=8080) 