import os
import time

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

upload_bp = Blueprint('upload', __name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['csv', 'xlsx']) 

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 442

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Nome do arquivo vazio'}), 442

    file_extension = file.filename.rsplit('.', 1)[1].lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        return jsonify({'error': 'Extensão de arquivo não suportada'}), 442

    #TODO: não armazenar localmente os arquivos
    filename = secure_filename(file.filename)
    new_filename = f'{filename.split(".")[0]}_{str(time.time())}.{file_extension}'
    save_location = os.path.join(UPLOAD_FOLDER, new_filename)

    file.save(save_location)

    return jsonify({'message': 'Planilha recebida com sucesso (POST)'}), 200
