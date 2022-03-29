from analytics.ml.cifar10 import cifar

from analytics.ml.mnist import forecaster as mnist_forecaster

def load_models():
    print("Loading ML modles")
    cifar.load_model()

def train_models():
    print("Training ML models")

def predict_cifar():
    cifar.predict()

def predcit_mnist(file_path):
    return mnist_forecaster.predict(file_path)