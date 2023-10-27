import numpy as np
import tensorflow as tf
import cv2
import pickle

class Prediction():
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = pickle.load(open('artifacts/chicken.pkl','rb'))
        preprocessor = pickle.load(open('artifacts/preprocessor.pkl','rb'))
        image = cv2.cvtColor(cv2.imread(self.filename), cv2.COLOR_BGR2RGB)
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = cv2.resize(image, (224, 224))
        image_pre = preprocessor(image)
        image_pre = np.expand_dims(image_pre, axis=0)
        result = np.argmax(model.predict(image_pre), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return[{"image" : prediction}]
        elif result[0] == 2:
            prediction = 'New Castle Disease'
            return [{"image" : prediction}]
        elif result[0] == 3:
            prediction = 'Salmonella'
            return [{"image" : prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{"image" : prediction}]