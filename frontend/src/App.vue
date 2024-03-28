<script setup>
import Upload from './components/Upload.vue'
import MrrChart from './components/MrrChart.vue'
import ChurnRateChart from './components/ChurnRateChart.vue'
</script>

<template>
  <main>
    <Upload />
    <br><br><br><br>
    <div class="charts">
      <MrrChart />
      <ChurnRateChart />
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