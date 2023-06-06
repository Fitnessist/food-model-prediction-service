from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import os
from PIL import Image
# from google.cloud import storage

app = Flask(__name__)

model = tf.keras.models.load_model("foodModel3.h5")
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Define class labels
# saya ingin mengambil data class label dari table foods kolom food_name
class_labels = [
    'ayam krispi',
    'bakso',
    'ikan goreng',
    'kopi',
    'mi ayam',
    'nasi goreng',
    'nasi putih',
    'nugget',
    'pecel',
    'roti tawar',
    'sate',
    'sayur sop',
    'sosis',
    'soto',
    'susu',
    'tahu',
    'teh',
    'telur dadar',
    'telur mata sapi',
    'tempe',
    'tumis kangkung'
]

# ini buat proses image kayak resize
def preprocess_image(image):
    # Preprocess the image as needed (e.g., resize, normalize, convert to array)
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image


@app.route('/predict', methods=['POST'])
def predict():
   # Get the image file from the request
    file = request.files['image']
    
    # Open and preprocess the image
    image = Image.open(file)
    preprocessed_image = preprocess_image(image)
    # Perform prediction using the loaded model
    prediction = model.predict(preprocessed_image)
    scores = tf.nn.softmax(prediction[0])
    
    # Get the top 5 predictions with highest confidence percentages
    top_predictions = []
    for i in np.argsort(scores)[-5:][::-1]:
        food_class = class_labels[i]
        confidence = float(100 * scores[i])  # Convert NumPy float to Python float
        prediction_entry = {
            'food_name': food_class,
            'confidence_percentage': confidence
        }
        top_predictions.append(prediction_entry)

    # Prepare the response JSON
    response = {
        'top_predictions': top_predictions
    }

    return jsonify(response)
