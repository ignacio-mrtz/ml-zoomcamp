import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('bees-wasps.h5', compile=False)

converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with open('bees-wasps-2.tflite', 'wb') as f_out:
    f_out.write(tflite_model)

#abro vscode desde mi terminal conda dentro de mi environment ml-zoomcamp que tiene descargado tensorflow(eso lo hago con: code) y luego en 
#terminal de vscode hago: python convert-model.py y me convierte el modelo a tflite