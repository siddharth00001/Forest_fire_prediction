import pickle
import numpy as np
import pandas as pd
from flask import Flask,request,jsonify,render_template
from sklearn.preprocessing import StandardScaler
application = Flask(__name__)
app = application
## import ridge regressor and Standard Scaler pickle
ridge_regressor = pickle.load(open('Models/ridge_model.pkl','rb'))
standard_scaler = pickle.load(open('Models/Scaler_model.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_regressor.predict(new_data_scaled)
        print(result)
        return render_template('home.html',result=result[0])
    else:
        return render_template('home.html')
if __name__=="__main__":
    app.run(host="0.0.0.0")
