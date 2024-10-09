<template>
  <div id="chart">
    <apexchart type="bubble" height="400" :options="chartOptions" :series="series"></apexchart>
  </div>
</template>

<script>
import apexchart from 'vue3-apexcharts';

export default {
  name: 'DataChart',
  components: {
    apexchart,
  },
  data() {
    return {
      chartOptions: {
        chart: {
          id: 'my-chart',
          type: 'bubble',
          height: 400,
        },
        xaxis: {
          tickAmount: 10,
          labels: {
            formatter: function(value) {
              return value.toFixed(0);
            },
            rotate: -45,
          },
        },
        yaxis: {
          max: 250,
          labels: {
            formatter: function(value) {
              return value.toFixed(0);
            },
          },
        },
        dataLabels: {
          enabled: false,
        },
      },
      series: [],
    };
  },
  async mounted() {
    try {
      const response = await fetch('http://localhost:8000/data');
      const data = await response.json();
      console.log('Fetched data:', data);
      this.series = [{
        name: 'Bubble Chart',
        data: data.values.map((value, index) => ({
          x: value.x,
          y: value.y,
          z: value.z,
          name: data.categories[index],
        })),
      }];
      console.log('Chart data:', this.series);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  },
};
</script>

