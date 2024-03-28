<script setup>
import Upload from './components/Upload.vue'
import MrrChart from './components/MrrChart.vue'
import ChurnRateChart from './components/ChurnRateChart.vue'
import { useChartData } from './stores/chart-data.js'

const chartDataStore = useChartData();

</script>

<template>
  <main>
    <Upload v-if="chartDataStore.chartData == null" />
    <div v-else class="charts">
      <MrrChart :data="chartDataStore.chartData.mrr" />
      <ChurnRateChart :data="chartDataStore.chartData.churns" />
    </div>
  </main>
</template>

<style scoped>
  .charts {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-items: center;
    justify-content: center;
  }
</style>