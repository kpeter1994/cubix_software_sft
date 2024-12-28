<script setup lang="ts">
  import Container from "~/components/Ui/Container.vue";
  import ChartComponent from "~/components/partials/ChartComponent.vue";
  import StockSearchComponent from "~/components/partials/StockSearchComponent.vue";
  import Card from "~/components/Ui/Card/Card.vue";
  import PortfolioList from "~/components/partials/PortfolioList.vue";

</script>

<template>
  <div class="py-6 lg:px-20 w-full">

      <div class="lg:flex w-full flex-wrap">
        <div class="lg:w-2/3 p-2">
          <h1 class="text-xl font-bold tracking-tight lg:text-2xl">Dashboard</h1>
          <StockSearchComponent/>
          <ChartComponent/>
        </div>
        <div class="lg:w-1/3 p-2">
          <PortfolioList/>
        </div>
      </div>

  </div>

</template>

<style scoped></style>
