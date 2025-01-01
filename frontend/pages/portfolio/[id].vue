<script setup lang="ts">
  import ChartComponent from "~/components/partials/ChartComponent.vue";
  import StockSearchComponent from "~/components/partials/StockSearchComponent.vue";
  import StockList from "~/components/partials/StockList.vue";
  import DeletePortfolio from "~/components/partials/DeletePortfolio.vue";

  const portfolioName = ref("");
</script>

<template>
  <div class="py-6 lg:px-20 w-full">

    <div class="lg:flex w-full flex-wrap">
      <div class="lg:w-2/3 p-2">
        <h1 class="text-xl font-bold tracking-tight lg:text-2xl">{{portfolioName}}</h1>
        <StockSearchComponent/>
        <ChartComponent/>
      </div>
      <div class="lg:w-1/3 p-2">
        <StockList v-model="portfolioName"/>
        <DeletePortfolio/>
      </div>
    </div>

  </div>

</template>

<style scoped></style>
