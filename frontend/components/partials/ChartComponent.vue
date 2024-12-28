<script setup lang="ts">

  const stockStore = useStockStore();
  const stock = computed(() => stockStore.stock);
  const path = computed(() =>
    `/stock/history-price?stock_symbol=${stock.value}&start=2024-01-01&end=2024-12-24`
  );
  const result : any = ref(null);
  const series : any = ref([]);
  const loading = ref(false);


  const fetchData = async () => {
    loading.value = true;
    const response : any = await useApiFetch(path.value, { method: "GET" });
    if (response && response.data) {
      series.value = [{ data: response.data }];
      result.value = response;
    }
    loading.value = false;
    return response;
  };

  await fetchData();


  const delay = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));


  watch(stock, async (newStock) => {
    await delay(1000);
    const response : any = await fetchData();

    if (response.error) {
      useSonner.error(response.error);
      loading.value = true;
    }
  });


  const chartOptions = computed(() => {
    return {
      chart: {
        type: "candlestick",
        height: 350,
      },
      title: {
        text: stock.value,
        align: "left",
      },
      xaxis: {
        type: "datetime",
      },
      yaxis: {
        tooltip: {
          enabled: true,
        },
      },
    };
  });

</script>

<template>

  <div>
    <div class="mb-3">
      <UiTabs>
        <UiTabsList :pill="false" class="relative grid w-full grid-cols-5">
          <UiTabsTrigger :pill="false" value="day">1 nap</UiTabsTrigger>
          <UiTabsTrigger :pill="false" value="week">1 hét</UiTabsTrigger>
          <UiTabsTrigger :pill="false" value="mounth">1 hónap</UiTabsTrigger>
          <UiTabsTrigger :pill="false" value="six-mounth">6 hónap</UiTabsTrigger>
          <UiTabsTrigger :pill="false" value="year">1 év</UiTabsTrigger>
          <UiTabsIndicator />
        </UiTabsList>
      </UiTabs>
    </div>
<!--    TODO make chart skeleton-->
    <div class="h-[350px] animate-pulse grid grid-cols-12 grid-rows-8" v-if="loading">
      <div class="col-span-2 row-span-7 flex flex-col justify-between">
        <div v-for="i in 8" class="w-full h-4 rounded bg-slate-100 animate-pulse"></div>
      </div>

    </div>
    <apexchart v-if="!loading"
               class="grow"
               type="candlestick"
               height="350"
               :options="chartOptions"
               :series="series"></apexchart>
  </div>

</template>



