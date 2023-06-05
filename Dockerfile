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

# Menjalankan aplikasi Flask
CMD ["python", "run.py"]