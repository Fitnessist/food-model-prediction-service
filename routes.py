from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)
model = tf.keras.models.load_model('models/model.h5')
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

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
