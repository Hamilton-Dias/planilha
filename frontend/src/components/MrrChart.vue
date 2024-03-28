<template>
  <div style="height: 100%; width: 50%;">
    <Bar
        id="mrr-chart"
        :options="chartOptions"
        :data="chartData"
    />
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const dados = {
  "2022-01":"272811.39",
  "2022-02":"189981.89",
  "2022-03":"158213.29",
  "2022-04":"81273.14",
  "2022-05":"79795.35",
  "2022-06":"80815.53",
  "2022-07":"58773.99",
  "2022-08":"60979.97",
  "2022-09":"44864.59"
}

export default {
  name: 'MrrChart',
  components: { Bar },
  computed: {
    chartData() {
      return {
        labels: Object.keys(dados),
        datasets: [
          {
            label: 'MRR',
            data: Object.values(dados),
          }
        ]
      }
    },
    chartOptions() {
      return {
        responsive: true,
        backgroundColor: "white"
      }
    }
  }
}
</script>