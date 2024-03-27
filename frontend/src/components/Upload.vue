<template>
  <form @submit.prevent="handleSubmit">
    <input id="fileInput" ref="fileInput" type="file" @change="handleFileChange">
    <p class="label">{{ textLabel }}</p>
    <button type="submit">{{ submitText }}</button>
    <p v-if="!!errorMessage" class="error-message">{{ errorMessage }}</p>
    <p v-if="!!successMessage" class="success-message">{{ successMessage }}</p>
  </form>
</template>

<script>

import { uploadFile } from "../services/api";

export default {
  data() {
    return {
      file: null,
      errorMessage: '',
      successMessage: '',
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
      this.successMessage = "";
    },
    async handleSubmit() {

      uploadFile(this.file)
          .then((response) => {
            this.successMessage = response.message;
            this.errorMessage = "";
          })
          .catch(error => {
            this.errorMessage = error;
            this.successMessage = "";
          })
          .finally(() => {
            this.resetFileInput();
          });

    },
    resetFileInput() {
      this.$refs.fileInput.value = '';
      this.file = null;
      this.fileName = '';
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

.success-message {
  color: green;
  margin-top: 10px;
}

</style>