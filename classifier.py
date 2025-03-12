import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Загрузка предобученной модели (например, ResNet, обученной на CIFAR-10)
model = load_model("models/cifar10_model.h5")
class_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

def classify_image(img_path):
    img = image.load_img(img_path, target_size=(32, 32))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    label_index = np.argmax(predictions)
    confidence = float(np.max(predictions))

    return class_names[label_index], confidence
