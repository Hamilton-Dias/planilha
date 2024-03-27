import axios from "axios";

export async function uploadFile(file) {
    return new Promise((resolve, reject) => {
        if (!file) {
            reject('Nenhum arquivo selecionado.');
        }

        const allowedExtensions = ['.xlsx', '.csv'];
        const fileExtension = file.name.split('.').pop().toLowerCase();
        if (!allowedExtensions.includes('.' + fileExtension)) {
            reject('Formato de arquivo não suportado. Por favor, escolha um arquivo .xlsx ou .csv.');
        }
    
        const formData = new FormData();
        formData.append("file", file);

        axios.post(process.env.VUE_APP_BACKEND_URL + "/upload", formData, {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        })
            .then((response) => {
                resolve(response.data);
            })
            .catch((error) => {
                reject(error);
            })
    });

}