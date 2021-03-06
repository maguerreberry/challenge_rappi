from flask import Blueprint, jsonify, request
import joblib
import pandas as pd
from titanic.predict import make_prediction
from api import __version__ as api_version

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/health', methods=['GET'])
def health():
    return 'ok'

@prediction_app.route('/predict', methods=['POST'])
def predict():
    json_data = request.get_json()

    X = pd.DataFrame(json_data)

    prediction = make_prediction(input_data=X)

    return jsonify(prediction)

@prediction_app.route('/version', methods=['GET'])
def version():
    return api_version
