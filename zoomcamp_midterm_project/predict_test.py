#!/usr/bin/env python
# coding: utf-8

import requests

url="http://localhost:9696/predict"
host_for_aws="sales-prediction-env.eba-fnayzkvs.us-west-2.elasticbeanstalk.com."
url_for_aws=f'http://{host_for_aws}/predict'

media_investments= {
    "tv_ad_budget":150.2,
    "radio_ad_budget":9.8,
    "newspaper_ad_budget":40.2
}

response=requests.post(url_for_aws,json=media_investments).json()

print(response)




