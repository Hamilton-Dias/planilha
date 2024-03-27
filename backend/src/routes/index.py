from flask import Blueprint

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return 'Servidor Flask rodando com sucesso!'