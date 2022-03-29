import tensorflow as tf
import numpy as np

from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

model_loaded = False
model = None

def load_model():
    global model_loaded
    global model
    if (model_loaded):
        return

    print("Loading MNIST Model")
    model = tf.keras.models.load_model('/Users/rajanp/work/ml-trainer/model_results/mnist/simple_convnet')
    print(model)

    model_loaded = True

def predict(file_path):
    global model
    load_model()

    img_height = 28
    img_width = 28
    img = tf.keras.utils.load_img(file_path, target_size=(img_height, img_width))
    r,g,b = img.split()
    img_array = tf.keras.utils.img_to_array(r)

    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print("1 >>", np.argmax(score))
    print("2 >>", np.max(score))

    return {
        "score": int(np.argmax(score))
    }
