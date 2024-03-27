from flask import Blueprint, request, jsonify

from .scripts.process_csv import process_csv
from .scripts.save_file import save_file_locally

upload_bp = Blueprint('upload', __name__)

ALLOWED_EXTENSIONS = set(['csv', 'xlsx']) 

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    success, response, status_code = validate_upload(request.files)
    if not success:
        return response, status_code

    try:
        saved_file_path = save_file_locally(request.files['file'])

        processed_data = process_csv(saved_file_path)
        return jsonify({'success': True, 'data': processed_data}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

def validate_upload(file):
    if 'file' not in request.files:
        return False, jsonify({'error': 'Nenhum arquivo enviado'}), 442

    file = request.files['file']

    if file.filename == '':
        return False, jsonify({'error': 'Nome do arquivo vazio'}), 442

    file_extension = file.filename.rsplit('.', 1)[1].lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        return False, jsonify({'error': 'Extensão de arquivo não suportada'}), 442

    return True, None, None