from flask import Flask
from routes.index import index_bp
from routes.upload import upload_bp

app = Flask(__name__)

app.register_blueprint(upload_bp)
app.register_blueprint(index_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)