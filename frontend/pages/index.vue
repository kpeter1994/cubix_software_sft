<script setup lang="ts">
  import Container from "~/components/Ui/Container.vue";
  import ChartComponent from "~/components/partials/ChartComponent.vue";
  import StockSearchComponent from "~/components/partials/StockSearchComponent.vue";

</script>

<template>
  <div class="p-6 w-full">

      <div class="flex w-full flex-wrap">
        <div class="w-2/3 p-2">
          <h1 class="text-xl font-bold tracking-tight lg:text-2xl">Dashboard</h1>
          <StockSearchComponent/>
        </div>
        <div class="w-1/3 p-2">

        </div>
        <div class="w-2/3">
          <ChartComponent/>
        </div>
      </div>

  </div>

</template>

<style scoped></style>
