<script lang="ts" setup>
  import CreatePortfolio from "~/components/partials/CreatePortfolio.vue";

  const portfolioList : any = ref([]);

  const portfolioStore = usePortfolioStore();

  onBeforeMount(async () => {
    const res : any = await portfolioStore.getAllPortfolios();
    if (!res.error){
      portfolioList.value = computed(() => portfolioStore.allPortfolio.portfolios);
    }

  });


</script>

<template>
  <div>
    <UiCard class="p-6 w-[400px] max-w-sm float-right">
      <div class="flex gap-1 items-center mb-6">
        <div class="bg-slate-50 rounded w-8 h-8 flex justify-center items-center border">
          <Icon name="ic:baseline-pie-chart" size="20" class="text-primary" />
        </div>

        <span class="text-xl">Potfoliók</span>
      </div>

      <div class="flex items-center justify-center">
        <UiList class="max-w-sm">
          <template v-for="p in portfolioStore.allPortfolio.portfolios" :key="p.id">
            <UiListItem class="items-start px-0">
              <UiListContent>
                <UiListTitle :title="p.name" />
                <UiListSubtitle
                  class="line-clamp-2"
                  :subtitle="p.description"
                />
              </UiListContent>
              <UiButton
                size="icon-sm"
                variant="ghost"
                :to="`/portfolio/${p.id}`"
                class="ml-auto shrink-0 self-center rounded-full"
              >
                <Icon name="lucide:chevron-right" />
              </UiButton>
            </UiListItem>
            <UiSeparator class="my-2.5 ml-auto w-[85%] last:hidden" />
          </template>
          <CreatePortfolio/>
        </UiList>
      </div>
    </UiCard>

  </div>
</template>

<style scoped></style>
