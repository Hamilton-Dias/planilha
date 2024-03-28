import { defineStore } from 'pinia'

export const useChartData = defineStore('chartData', {
   state: () => ({
      chartData: null
   }),
   actions: {
      setChartData(data) {
         this.chartData = data
      }
   }
});