from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnnClassifier.pipeline.prediction import Prediction
from cnnClassifier.utils.common import decodeImage
import pickle

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = 'inputImage.jpg'
        self.classifier = Prediction(
            filename=self.filename
        )

@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)



if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)