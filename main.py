from flask import Flask
from app.predictions.predict.routes import predict_bp

app = Flask(__name__)

# Daftarkan blueprint untuk prediksi
app.register_blueprint(predict_bp)

if __name__ == '__main__':
    app.run()
