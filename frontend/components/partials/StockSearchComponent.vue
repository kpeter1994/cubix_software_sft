<script setup lang="ts">

  import InicatorDropdown from "~/components/partials/InicatorDropdown.vue";
  import { useStockStore } from "~/stores/stock";

  const selectedStock = ref(null);
  const stockStore = useStockStore()

  const options = [
    { name: "AAPL", description: "Apple Inc.", id: 1 },
    { name: "GOOGL", description: "Alphabet Inc.", id: 2 },
    { name: "AMZN", description: "Amazon.com Inc.", id: 3 },
    { name: "MSFT", description: "Microsoft Corporation", id: 4 },
    { name: "TSLA", description: "Tesla Inc.", id: 5 },
    { name: "META", description: "Meta Platforms Inc.", id: 6 },
    { name: "NFLX", description: "Netflix Inc.", id: 7 },
    { name: "NVDA", description: "NVIDIA Corporation", id: 8 },
    { name: "BRK.B", description: "Berkshire Hathaway Inc.", id: 9 },
    { name: "JPM", description: "JPMorgan Chase & Co.", id: 10 },
    { name: "V", description: "Visa Inc.", id: 11 },
  ];

  const formattedOptions = options.map((option) => ({
    ...option,
    formattedLabel: `${option.name} - ${option.description || ''}`.trim(),
  }));

  watch(selectedStock, (newValue : any) => {
    stockStore.setStock(newValue);
  });



</script>

<template>
  <div class="flex items-center gap-3 justify-between">
    <UiVeeMultiSelect
      class="max-w-xl"
      searchable
      value-prop="name"
      v-model="selectedStock"
      label="formattedLabel"
      placeholder="Keresés a részvények között"
      :options="formattedOptions"
    />
    <InicatorDropdown/>
  </div>
</template>


