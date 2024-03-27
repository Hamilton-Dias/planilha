import os
import time
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_file_locally(file):
    #TODO: não armazenar localmente os arquivos - usar Cloud Storage se realmente fosse necessário armazenar
    filename = secure_filename(file.filename)
    file_extension = filename.rsplit('.', 1)[1].lower()
    new_filename = f'{filename.split(".")[0]}_{str(time.time())}.{file_extension}'
    save_location = os.path.join(UPLOAD_FOLDER, new_filename)
    file.save(save_location)
    return save_location