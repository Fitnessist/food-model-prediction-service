from google.cloud import storage

client = storage.Client()

# Mendownload model dari GCS
bucket_name = "nama_bucket_anda"
blob_name = "models/foodModel1.h5"
model_path = "/tmp/foodModel1.h5"  # Path sementara untuk menyimpan model
bucket = client.get_bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.download_to_filename(model_path)