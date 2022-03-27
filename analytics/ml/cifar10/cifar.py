import tensorflow as tf
import numpy as np

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

model = tf.keras.models.load_model('/Users/rajanp/work/ml-trainer/model_results/cifar10')

def load_model():
    print("Loading CIFAR Model")
    print(model)

def predict():
    img_height = 32
    img_width = 32
    img = tf.keras.utils.load_img(
        "/Users/rajanp/Downloads/test/299153.png", target_size=(img_height, img_width)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(np.argmax(score))
    print(np.max(score))
