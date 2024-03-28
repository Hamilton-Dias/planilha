<template>
  <div style="height: 100%; width: 50%;">
    <Bar
        id="churn-rate-chart"
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
  "2022-01":"122",
  "2022-02":"77",
  "2022-03":"44",
  "2022-04":"34",
  "2022-05":"36",
  "2022-06":"34",
  "2022-07":"23",
  "2022-08":"20",
  "2022-09":"5"
}

export default {
  name: 'ChurnRateChart',
  components: { Bar },
  computed: {
    chartData() {
      return {
        labels: Object.keys(dados),
        datasets: [
          {
            label: 'Churn Rate',
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