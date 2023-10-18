import pickle

from flask import Flask
from flask import request
from flask import jsonify 

model_file="model1.bin"
dv_file='dv.bin'

with open(model_file,'rb') as mf_in:
    model=pickle.load(mf_in)

with open(dv_file,'rb') as df_in:
    dv=pickle.load(df_in)


#client={"job": "retired", "duration": 445, "poutcome": "success"}

app=Flask('credit') 

@app.route('/predict',methods=['POST'])#post because we want to send some information about the customer 

def predict():
    client=request.get_json()
    X=dv.transform([client])
    y_pred=model.predict_proba(X)[0,1]
    result= { 
        'credit probability':float(y_pred),
    } 
    return jsonify(result) 

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=9696) 