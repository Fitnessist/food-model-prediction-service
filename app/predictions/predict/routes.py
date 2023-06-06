from flask import Blueprint, request, jsonify
from app.predictions.predict.service import predict_image

predict_bp = Blueprint('predict', __name__, url_prefix='/predict')

@predict_bp.route('/', methods=['POST'])
def predict():
    # Get the image file from the request
    file = request.files['image']

    # Perform prediction using the image
    result = predict_image(file)

    # Prepare the response JSON
    response = {
        'prediction': result
    }

    return jsonify(response)

