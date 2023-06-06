# Menggunakan image base Python
FROM python:3.9-slim

# Mengatur working directory di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Menginstal dependensi yang diperlukan
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh isi proyek ke dalam container
COPY . .

# Menetapkan argumen untuk variabel lingkungan yang diperlukan
ARG DATABASE_HOST_ARG
ENV DATABASE_HOST=$DATABASE_HOST_ARG

ARG DATABASE_PORT_ARG
ENV DATABASE_PORT=$DATABASE_PORT_ARG

ARG DATABASE_NAME_ARG
ENV DATABASE_NAME=$DATABASE_NAME_ARG

ARG DATABASE_USERNAME_ARG
ENV DATABASE_USERNAME=$DATABASE_USERNAME_ARG

ARG DATABASE_PASSWORD_ARG
ENV DATABASE_PASSWORD=$DATABASE_PASSWORD_ARG

ARG GCS_BUCKET_NAME_ARG
ENV GCS_BUCKET_NAME=$GCS_BUCKET_NAME_ARG

ARG GCS_MODEL_FILE_NAME_ARG
ENV GCS_MODEL_FILE_NAME=$GCS_MODEL_FILE_NAME_ARG

EXPOSE 8080

# Menjalankan aplikasi Flask
CMD ["python", "main.py"]
