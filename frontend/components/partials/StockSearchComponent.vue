<script setup lang="ts">

  const selectedStock = ref('AAPL');
  const stockStore = useStockStore();


</script>

<template>
  <div class="flex items-center gap-3 justify-between">
    <div class="flex gap-1 items-center">
      <UiInput
        class="max-w-xl"
        v-model="selectedStock"
      />
      <UiButton @click="stockStore.setStock(selectedStock)">Keresés</UiButton>
    </div>

  </div>
</template>


