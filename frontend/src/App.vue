<template>
  <main>
    <Upload v-if="chartDataStore.chartData == null" />
    <div v-else class="charts">
      <button @click="clearChartData">Voltar e inserir outra planilha</button>
      <MrrChart :data="chartDataStore.chartData.mrr" />
      <ChurnRateChart :data="chartDataStore.chartData.churns" />
    </div>
  </main>
</template>

<script setup>
import Upload from './components/Upload.vue'
import MrrChart from './components/MrrChart.vue'
import ChurnRateChart from './components/ChurnRateChart.vue'
import { useChartData } from './stores/chart-data.js'
import { onMounted } from 'vue'

const chartDataStore = useChartData();

const clearChartData = () => {
  chartDataStore.setChartData(null);
}

onMounted(() => {
  document.title = 'Exemplo Planilha';
});
</script>

<style scoped>
  button {
    position: absolute;
    top: -40px;
    left: 0;

    margin: 0;
    color: var(--white);
    background: var(--green-500);
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    border-bottom: 4px solid var(--green-500);
    transition: all .2s ease;
    outline: none;
  }

  .charts {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-items: center;
    justify-content: center;
    position: relative;
    width: 100%;
  }

  .charts > * {
    flex: 1;
  }
</style>