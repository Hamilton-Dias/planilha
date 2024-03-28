<template>
  <div style="height: 100%; width: 50%;">
    <Line
        id="churn-rate-chart"
        :options="chartOptions"
        :data="chartData"
    />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

const props = defineProps({
  data: {
    type: Object,
    required: true
  }
})

const chartData = computed(() => {
  return {
    labels: Object.keys(props.data),
    datasets: [
      {
        label: 'Churn Rate',
        data: Object.values(props.data),
      }
    ]
  }
})

const chartOptions = {
  responsive: true,
  backgroundColor: '#f87979',
}
</script>