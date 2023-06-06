import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Konfigurasi koneksi database dari environment variables
DB_HOST = os.getenv('DATABASE_HOST', 'localhost')
DB_PORT = os.getenv('DATABASE_PORT', '5432')
DB_NAME = os.getenv('DATABASE_NAME', 'fitnessist-db')
DB_USER = os.getenv('DATABASE_USERNAME', 'postgres')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD', 'root')

# Buat URL koneksi database
DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Buat objek engine SQLAlchemy
engine = create_engine(DB_URL, echo=True)

# Buat objek sesi database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Buat objek BaseModel untuk deklarasi model SQLAlchemy
Base = declarative_base()

# Fungsi untuk mendapatkan objek sesi database
def get_db():
    db = SessionLocal()
    try:
        return db
    except:
        db.close()
        raise
