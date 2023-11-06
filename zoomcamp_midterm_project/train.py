#!/usr/bin/env python
# coding: utf-8

import xgboost as xgb
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle

df=pd.read_csv("./data/Advertising_Budget_and_Sales.csv")

#DATA PREPARATION:

df.columns=df.columns.str.lower().str.replace(' ','_')

new_column_names = {
    'tv_ad_budget_($)': 'tv_ad_budget',
    'radio_ad_budget_($)': 'radio_ad_budget',
    'newspaper_ad_budget_($)': 'newspaper_ad_budget',
    'sales_($)':'sales'
}

df = df.rename(columns=new_column_names)

del df['unnamed:_0']
#DELETING OUTLIERS:

outliers=df[df.newspaper_ad_budget>90]
outlier_index=df[df.newspaper_ad_budget>90].index
df.drop(outlier_index,inplace=True)

#SPLITTING THE DATASET:

df_full_train, df_test=train_test_split(df, test_size=0.2,random_state=1)

df_full_train=df_full_train.reset_index(drop=True)
df_test=df_test.reset_index(drop=True)

y_full_train=df_full_train.sales.values
y_test=df_test.sales.values

del df_full_train['sales']
del df_test['sales']

X_full_train=df_full_train.values
X_test=df_test.values

print("Dataset splitting is performed")

# TRAINING THE FINAL MODEL WITH XGBOOST:

features = df_full_train.columns.tolist()

dtrain = xgb.DMatrix(X_full_train, label=y_full_train, feature_names=features)
dtest = xgb.DMatrix(X_test, label=y_test, feature_names=features)

xgb_params = {
    'eta': 0.3, 
    'max_depth': 7,
    'min_child_weight': 1,

    'objective': 'reg:squarederror',
    'eval_metric': 'rmse',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}

final_model = xgb.train(xgb_params, dtrain, num_boost_round=20)

print("model trained")

# save the model:

output_file=f'model_midterm_project.bin'

with open(output_file,'wb') as f_out:
    pickle.dump((features,final_model), f_out)







