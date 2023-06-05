from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import os
from PIL import Image
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".credentials\credential.json"

app = Flask(__name__)
client = storage.Client()

# Mendownload model dari GCS
bucket_name = "bucket-training-model"
blob_name = "foodModel1.h5"
model_path = "/tmp/foodModel1.h5"  # Path sementara untuk menyimpan model
bucket = client.get_bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.download_to_filename(model_path)

model = tf.keras.models.load_model(model_path)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# hapus model sementara
os.remove(model_path)

# Define class labels
class_labels = ['class1', 'class2', 'class3', 'class4', 'class5']

def preprocess_image(image):
    # Preprocess the image as needed (e.g., resize, normalize, convert to array)
    image = image.resize((180, 180))
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
    prediction = model.predict(data)

    # Process the prediction result (if needed)
    predicted_class = class_labels[np.argmax(predictions)]
    
    return jsonify({'prediction': predicted_class})
