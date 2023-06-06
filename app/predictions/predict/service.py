import tensorflow as tf
import os
import numpy as np
from PIL import Image
from app.infrastructure.storage import download_model
from app.infrastructure.database import Base, get_db
from app.predictions.food.model import Food

# Load the model from Google Cloud Storage
model_path = download_model()
# model_path = "temp/model/model.h5"
model = tf.keras.models.load_model(model_path)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Perform prediction on the image
def perform_prediction(class_labels, image):
    preprocessed_image = preprocess_image(image)
    prediction = model.predict(preprocessed_image)
    scores = tf.nn.softmax(prediction[0])
    
    top_predictions = []
    for i in np.argsort(scores)[-5:][::-1]:
        food_class = class_labels[i]
        confidence = float(100 * scores[i])
        prediction_entry = {
            'food': food_class,
            'confidence_percentage': confidence
        }
        top_predictions.append(prediction_entry)

    return top_predictions

# Get class labels from the database
def get_class_labels():
    foods = Food.get_food_list()
    # class_labels = [food['food_name'] for food in foods]

    return foods

# Predict endpoint
def predict_image(file):
    class_labels = get_class_labels()
    predictions = perform_prediction(class_labels, file)

    return predictions
