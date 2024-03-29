<template>
  <div class="chart-container">
    <Line
      :options="chartOptions"
      :data="chartData"
    />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js'
import { formatLabel } from '../utils/utils.js'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

const props = defineProps({
  data: {
    type: Object,
    required: true
  }
})

const chartData = computed(() => {
  return {
    labels: Object.keys(props.data).map(formatLabel),
    datasets: [
      {
        label: 'Monthly Recurring Revenue',
        data: Object.values(props.data),
      }
    ]
  }
})

const chartOptions = {
  responsive: true,
  backgroundColor: '#599c54',
  borderColor: "#599c54",
  tension: 0.3,
  pointRadius: 0,
  scales: {
    y: {
      border: {
        dash: [5, 10],
      },
      grid: {
        drawTicks: false,
      }
    },
    x: {
      grid: {
        display: false,
      },
      border: {
        display: false,
      }
    },
  },
}
</script>

<style scoped>
  .chart-container {
    height: 100%; 
    width: 50%;
    margin-bottom: 20px;
  }

  @media screen and (max-width: 1000px) {
    .chart-container {
      width: 100%;
    }
    
  }
</style>