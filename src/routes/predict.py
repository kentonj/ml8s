from flask import Blueprint, request, jsonify
import os
import pickle
import pandas as pd
# required import so that we can pickle load an object of this class
from src.training.iris_classifier.pipeline import IrisClassifier

predict = Blueprint('models', __name__, url_prefix='/predict')

# load the model
iris_model_path = 'src/models/iris_classifier.model'
with open(iris_model_path, 'rb') as f:
    iris_model = pickle.load(f)

@predict.route('/iris', methods=['POST'])
def predict_iris():
    """Load the digits recommender model, and predict based on the data provided."""
    request_body = request.json
    payload = request_body.get('payload')
    # ensure that we have the payload
    if not isinstance(payload, list):
        response = jsonify({'err': 'no either no payload, or payload is not a list'})
        response.status_code = 400
        return response
    else:
        predictions = iris_model.predict(payload)
        response = jsonify({'predictions': predictions})
        response.status_code = 200
        return response
