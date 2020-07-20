from flask import Blueprint, request, jsonify
import os
import pickle
import pandas as pd

digit_model_path = 'src/models/iris_classifier.model'
with open(digit_model_path, 'rb') as f:
    digit_model = pickle.load(f)

models = Blueprint('models', __name__, url_prefix='/models')
@models.route('/predict/iris', methods=['POST'])
def predict_iris():
    """Load the digits recommender model, and predict based on the data provided."""
    request_body = request.json
    payload = request_body.get('payload')
    # ensure that we have the payload
    if payload is None:
        response = jsonify({'err': 'no payload key found in POST body'})
        response.status_code = 400
        return response
    df = pd.DataFrame(payload)
    print(df)
    print(f'here is the request body: \n{request_body}')
    return jsonify({'msg': f'requested model'})
