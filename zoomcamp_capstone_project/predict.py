# load the model:

import pickle

import xgboost as xgb
from flask import Flask
from flask import request
from flask import jsonify 

input_file=f'model_capstone_project.bin'

with open(input_file,'rb') as f_in:
    dv, model=pickle.load(f_in)

app=Flask('reached_on_time') 

@app.route('/predict',methods=['POST'])

def predict():
    sale_data=request.get_json()
    X_sale_data = dv.transform(sale_data)
    features = list(dv.get_feature_names_out())
    d_X = xgb.DMatrix(X_sale_data, feature_names=features)
    y_pred = model.predict(d_X)[0]
    reach_on_time=y_pred<0.5
    result= { 
        'probability_of_not_reaching_on_time':float(y_pred),
        'reach_on_time': bool(reach_on_time)
    }
    return jsonify(result) 

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=9696) 