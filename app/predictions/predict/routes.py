from flask import Blueprint, request, jsonify
import base64
from io import BytesIO
from PIL import Image
from app.predictions.predict.service import predict_image

predict_bp = Blueprint('predict', __name__)

@predict_bp.post('/predict')
def predict():
   # Get the image data from the request
    data = request.get_json()
    image_data = data.get('image')

    # Decode the base64 image data
    image_bytes = base64.b64decode(image_data)

    # Open the image using PIL
    image = Image.open(BytesIO(image_bytes))

    # Perform prediction using the image
    result = predict_image(image)

    # Prepare the response JSON
    response = {
        'status' : {
            'code' : 200,
            'message' : 'OK'
        },
        'data': {'predictions': result}
    }

    return jsonify(response)

