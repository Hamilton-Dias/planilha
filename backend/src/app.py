from flask import Flask
from routes.upload import upload_bp

app = Flask(__name__)

app.register_blueprint(upload_bp)

@app.route('/')
def index():
    return 'Servidor Flask rodando com sucesso!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)