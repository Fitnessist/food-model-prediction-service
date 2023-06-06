import os
from google.cloud import storage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the environment variables for credential path, bucket name, and model file name
credential_path = "credentials/credential.json"
bucket_name = os.getenv('GCS_BUCKET_NAME', "bucket-training-model")
model_file_name = os.getenv('GCS_MODEL_FILE_NAME', "model/foodModel1.h5")

def download_model():
    # Create a storage client and specify the credential file
    storage_client = storage.Client.from_service_account_json(credential_path)

    # Get the bucket
    bucket = storage_client.get_bucket(bucket_name)

    # Define the path to the model file in the bucket
    model_blob = bucket.blob(model_file_name)

    # Specify the local directory path to save the downloaded model
    local_directory = 'temp/model'

    # Create the local directory if it doesn't exist
    os.makedirs(local_directory, exist_ok=True)

    # Specify the local path to save the downloaded model
    local_model_path = os.path.join(local_directory, 'model.h5')

    # Download the model file from the bucket
    model_blob.download_to_filename(local_model_path)

    return local_model_path
