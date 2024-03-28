<template>
  <form @submit.prevent="handleSubmit">
    <input id="fileInput" ref="fileInput" type="file" @change="handleFileChange">
    <p class="label">{{ textLabel }}</p>
    <button type="submit">{{ submitText }}</button>
    <p v-if="!!errorMessage" class="error-message">{{ errorMessage }}</p>
    <p v-if="!!successMessage" class="success-message">{{ successMessage }}</p>
  </form>
</template>

<script setup>

import { ref, computed } from 'vue';
import { uploadFile } from "../services/api";
import { useChartData } from '../stores/chart-data.js';

const chartDataStore = useChartData();

const file = ref(null);
const errorMessage = ref('');
const successMessage = ref('');
const fileName = ref('');

const text = 'Arraste a sua planilha ou clique aqui.';
const submitText = 'Enviar';

const textLabel = computed(() => {
  return file.value ? 'Arquivo selecionado: ' + fileName.value : text;
});

const handleFileChange = (event) => {
  file.value = event.target.files[0];
  fileName.value = file.value.name;
  errorMessage.value = "";
  successMessage.value = "";
};

const handleSubmit = async () => {
  try {
    const response = await uploadFile(file.value);
    chartDataStore.setChartData(response.data);
    successMessage.value = response.message;
    errorMessage.value = "";
  } catch (error) {
    errorMessage.value = error;
    successMessage.value = "";
  } finally {
    resetFileInput();
  }
};

const resetFileInput = () => {
  file.value = null;
  fileName.value = '';
};

</script>

<style scoped>
form {
  width: 50%;
  height: 200px;
  border: 4px dashed var(--gray-500);
  position: relative;
  margin: 0 auto;
}

form > .label {
  width: 100%;
  height: 100%;
  text-align: center;
  line-height: 170px;
  color: var(--gray-700);
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
  color: var(--white);
  background: var(--green-500);
  border: none;
  width: calc(100% + 8px);
  height: 35px;
  margin-left: -4px;
  border-radius: 4px;
  border-bottom: 4px solid var(--green-500);
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
  color: var(--red-500);
  margin-top: 10px;
}

.success-message {
  color: var(--green-500);
  margin-top: 10px;
}

</style>