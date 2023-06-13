# Fitnessist Food Model Prediction Service

The Fitnessist Food Model Prediction Service is a Python application that serves the trained TensorFlow model (`model.h5`) that stored on Google Cloud Storage. It provides an API endpoint to make food image predictions based on the trained model.

## Prerequisites

Before deploying the service, make sure you have the following prerequisites installed and set up:

- Python 3.x
- TensorFlow
- Flask
- Docker
- Google Cloud SDK
- Google Cloud Run

## Installation

1. Clone the repository:

   ```shell
   $ git clone https://github.com/Fitnessist/food-model-prediction-service.git
   $ cd food-model-prediction-service
   ```

2. Install the required dependencies:

   ```shell
   $ pip install -r requirements.txt
   ```

3. Place your trained TensorFlow model (`model.h5`) in the `model` directory.

## Local Testing

To test the service locally, use the following steps:

1. Set the environment variables:

   ```shell
   $ export PROJECT_ID=your-project-id
   ```

2. Run the Flask development server:

   ```shell
   $ python app.py
   ```

3. The service will be accessible at `http://localhost:5000`.

## Deployment to Google Cloud Run

To deploy the service to Google Cloud Run, follow these steps:

1. Set up your Google Cloud project and authenticate with the Google Cloud SDK:

   ```shell
   $ gcloud config set project your-project-id
   $ gcloud auth login
   ```

2. Build and upload the Docker image to Google Container Registry:

   ```shell
   $ gcloud builds submit --tag gcr.io/your-project-id/food-model-prediction-service
   ```

3. Deploy the service to Google Cloud Run:

   ```shell
   $ gcloud run deploy --image gcr.io/your-project-id/food-model-prediction-service --platform managed --allow-unauthenticated
   ```

4. After deployment, you will receive a URL where the service is accessible.

## Usage

Once the service is deployed, you can make POST requests to the API endpoint to make food image predictions. The endpoint URL will be provided after the deployment.

Here is an example using cURL:

```shell
$ curl -X POST -F 'image=@food.jpg' https://your-service-url/predict
```

Replace `food.jpg` with the path to your food image.

The API will return the predicted class and probability for the given food image.

## Technologies and Libraries

The Fitnessist Food Model Prediction Service uses the following technologies and libraries:

- Python: The programming language used for developing the service.
- TensorFlow: An open-source machine learning framework for building and deploying ML models.
- Flask: A lightweight web framework for creating RESTful APIs.
- Docker: A platform for building, deploying, and running applications using containers.
- Google Cloud Run: A serverless execution environment for deploying and scaling containerized applications.
- Google Container Registry: A private container image registry for storing and managing Docker images.
