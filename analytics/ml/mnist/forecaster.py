import tensorflow as tf
import numpy as np

from analytics.ml.mnist import simple_convnet_forecaster

def predict(file_path):
    results = []
    convnet_forecast = simple_convnet_forecaster.predict(file_path)
    results.append(convnet_forecast)
    return results
