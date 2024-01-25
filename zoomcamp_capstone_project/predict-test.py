#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests

#url="http://localhost:9696/predict"
host_for_aws="shipping-serving-env.eba-6ip2ev52.us-west-2.elasticbeanstalk.com."
url_for_aws=f'http://{host_for_aws}/predict'

sale_data= {
    "warehouse_block": "F", 
    "mode_of_shipment": "Ship", 
    "customer_rating": 1, 
    "product_importance": "high", 
    "gender": "F", 
    "customer_care_calls": 6, 
    "cost_of_the_product": 168, 
    "prior_purchases": 5, 
    "discount_offered": 65, 
    "weight_in_gms": 1601
}

response=requests.post(url_for_aws,json=sale_data).json()

print(response)


# In[ ]:




