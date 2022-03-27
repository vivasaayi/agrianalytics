from analytics.ml.cifar10 import cifar

def load_models():
    print("Loading ML modles")
    cifar.load_model()

def train_models():
    print("Training ML models")

def predict_cifar():
    cifar.predict()