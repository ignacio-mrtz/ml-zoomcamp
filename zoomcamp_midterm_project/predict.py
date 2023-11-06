# load the model:

import pickle

import xgboost as xgb
from flask import Flask
from flask import request
from flask import jsonify 

input_file=f'model_midterm_project.bin'

with open(input_file,'rb') as f_in:
    features, model=pickle.load(f_in)

app=Flask('credit') 

@app.route('/predict',methods=['POST'])

def predict():
    media_investments=request.get_json()
    X=[list(media_investments.values())]
    d_X = xgb.DMatrix(X, feature_names=features)
    y_pred = model.predict(d_X)[0]
    result= { 
        'sales':float(y_pred),
    } 
    return jsonify(result) 

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=9696) 