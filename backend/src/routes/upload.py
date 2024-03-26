from flask import Blueprint, request, jsonify

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Nome do arquivo vazio'}), 400

    # Processa a planilha
    # TODO: Adicione a lógica para processar a planilha

    return jsonify({'message': 'Planilha recebida com sucesso (POST)'}), 200
