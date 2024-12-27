<script setup lang="ts">
  const path = ref("/stock/history-price?stock_symbol=ACHR&start=2024-11-01&end=2024-12-24")
  const result : any = ref(null);
  const series = ref([]);

  const fetchData = async () => {
    const response = await useApiFetch(path.value, { method: "GET" });
    if (response && response.data) {
      series.value = [{ data: response.data }];
      result.value = response;
    }
  };

  await fetchData();


  const delay = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

  watch(path, async (newPath) => {
    await delay(900);
    await fetchData();
  });




  const chartOptions = {
    chart: {
      type: 'candlestick',
      height: 350
    },
    title: {
      text: 'CandleStick Chart',
      align: 'left'
    },
    xaxis: {
      type: 'datetime'
    },
    yaxis: {
      tooltip: {
        enabled: true
      }
    }
  }

</script>

<template>

  <div>
    <UiInput v-model="path"></UiInput>
  </div>


  <apexchart class="w-full" type="candlestick" height="350" :options="chartOptions" :series="series"></apexchart>
</template>



