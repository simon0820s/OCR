import numpy as np
from keras.applications import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from PIL import Image

def run(img):
    # Cargar el modelo preentrenado VGG16 sin la capa final (clasificación)
    base_model = VGG16(weights='imagenet', include_top=True)

    # Realizar la predicción de calidad de imagen
    pred = base_model.predict(img)
    print("pred: ",pred)

    # Interpretar la predicción
    if pred[0] < 0.5:
        print("La imagen es de baja calidad.")
    else:
        print("La imagen es de buena calidad.")

if __name__=='__main__':
    run()