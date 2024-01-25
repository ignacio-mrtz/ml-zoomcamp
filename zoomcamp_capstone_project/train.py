#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
import xgboost as xgb
import pickle

df=pd.read_csv("./data/ecom_shipping.csv")

df.columns=df.columns.str.lower()

df.rename(columns={'reached.on.time_y.n': 'reached_on_time'}, inplace=True)

df.drop('id', axis=1, inplace=True)

# classifying features into categorical and numerical:
numerical = ['customer_care_calls', 'cost_of_the_product', 'prior_purchases', 'discount_offered', 'weight_in_gms' ]
categorical = ['warehouse_block', 'mode_of_shipment','customer_rating', 'product_importance', 'gender']


# Splitting the data 

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train.reached_on_time.values
y_test = df_test.reached_on_time.values


del df_full_train['reached_on_time']
del df_test['reached_on_time']

dv = DictVectorizer(sparse=False)

dicts_full_train = df_full_train.to_dict(orient='records')
X_full_train = dv.fit_transform(dicts_full_train)

print("Dataset splitting is performed")

### training the model with xgboost

features = list(dv.get_feature_names_out())

dfulltrain = xgb.DMatrix(X_full_train, label=y_full_train,
                    feature_names=dv.get_feature_names_out())

xgb_params = {
    'eta': 0.1, 
    'max_depth': 5,
    'min_child_weight': 10,

    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}

final_model = xgb.train(xgb_params, dfulltrain, num_boost_round=10)

print("model trained")

# save the model:

output_file=f'model_capstone_project.bin'

with open(output_file,'wb') as f_out:
    pickle.dump((dv,final_model), f_out)
