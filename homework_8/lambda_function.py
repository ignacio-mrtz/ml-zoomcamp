#!/usr/bin/env python
# coding: utf-8

#import tensorflow.lite as tflite
import tflite_runtime.interpreter as tflite
from io import BytesIO
from urllib import request
import numpy as np
from PIL import Image
import os



MODEL_NAME = os.getenv('MODEL_NAME' ,'bees-wasps-2.tflite')#I set this model as default unless i specify another model in the dockerfile

interpreter = tflite.Interpreter(model_path=MODEL_NAME)
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

#print(f'output index: {output_index}')




def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img


def preprocess_input(x):
    return x / 255.0



#url = 'https://habrastorage.org/webt/rt/d9/dh/rtd9dhsmhwrdezeldzoqgijdg8a.jpeg'
def predict(url):
    image=download_image(url)
    image_2=prepare_image(image,target_size=(150,150))
    x=np.array(image_2, dtype='float32')
    X=np.array([x])
    X=preprocess_input(X)
    value_q3=X[0,0,0,0]
    #print(value_q3)
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    float_predictions = preds[0].tolist()
    return float_predictions


def lambda_handler(event, context):
    url = event['url']
    pred = predict(url)
    result = {
        'prediction': pred
    }
    return result

#answers: 
#q1)43 mb
#q2)13
#q3)0.9450980392156862
#q4)0.65898407
#q5)c
#q6)0.4453
