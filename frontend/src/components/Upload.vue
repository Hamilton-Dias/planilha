<template>
  <form @submit.prevent="handleSubmit">
    <input id="fileInput" ref="fileInput" type="file" @change="handleFileChange">
    <p class="label">{{ textLabel }}</p>
    <button type="submit">{{ submitText }}</button>
    <p v-if="!!errorMessage" class="error-message">{{ errorMessage }}</p>
  </form>
</template>

<script>
export default {
  data() {
    return {
      file: null,
      errorMessage: '',
      fileName: ''
    };
  },
  props: {
    text: {
      type: String,
      default: 'Arraste a sua planilha ou clique aqui.'
    },
    submitText: {
      type: String,
      default: 'Enviar'
    }
  },
  computed: {
    textLabel() {
      return this.file ? 'Arquivo selecionado: ' + this.fileName : this.text;
    }
  },
  methods: {
    handleFileChange(event) {
      this.file = event.target.files[0];
      this.fileName = this.file.name;
      this.errorMessage = "";
    },
    async handleSubmit() {
      if (!this.file) {
        this.errorMessage = 'Por favor, escolha um arquivo.';
        return;
      }

      const allowedExtensions = ['.xlsx', '.csv'];
      const fileExtension = this.file.name.split('.').pop().toLowerCase();
      if (!allowedExtensions.includes('.' + fileExtension)) {
        this.errorMessage = 'Formato de arquivo não suportado. Por favor, escolha um arquivo .xlsx ou .csv.';
        return;
      }

      try {
        const formData = new FormData();
        formData.append('file', this.file);

        // Aqui você pode fazer uma requisição para o servidor para enviar o arquivo
        // Exemplo usando fetch:
        // const response = await fetch('URL_DO_SEU_ENDPOINT', {
        //   method: 'POST',
        //   body: formData
        // });
        // console.log('Upload successful', response);

        this.file = null;
        this.errorMessage = '';

      } catch (error) {
        console.error('Erro ao fazer upload', error);
        this.errorMessage = 'Ocorreu um erro ao fazer upload do arquivo.';
      }
    }
  }
};
</script>

<style scoped>
form {
  width: 500px;
  height: 200px;
  border: 4px dashed var(--white);
  position: relative;
}

form > .label {
  width: 100%;
  height: 100%;
  text-align: center;
  line-height: 170px;
  color: var(--white);
  font-family: Arial;
}

form > input {
  position: absolute;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  outline: none;
  opacity: 0;
}

form > button {
  margin: 0;
  color: #fff;
  background: #16a085;
  border: none;
  width: 508px;
  height: 35px;
  margin-top: -20px;
  margin-left: -4px;
  border-radius: 4px;
  border-bottom: 4px solid var(#117A60);
  transition: all .2s ease;
  outline: none;
}
form > button:hover{
  filter: brightness(90%);
}
form > button:active{
  border:0;
}

.error-message {
  color: red;
  margin-top: 10px;
}
</style>