<script lang="ts" setup>
  import AddStock from "~/components/partials/AddStock.vue";
  import DeleteShare from "~/components/partials/DeleteShare.vue";

  const portfolioStore = usePortfolioStore();
  const route : any = useRoute()
  const shares : any = ref(null);
  const id : number = Number(route.params.id);
  const refresh = ref(false);
  const portfolioName = defineModel()

  const fetchShares = async (id: number) =>{
   try {
     const res : any = await portfolioStore.getSharesForPortfolio(id);
     portfolioName.value = res.portfolio_details.portfolio_name;
     const { error } = res;
     if (error){
       useSonner.error(error);
       shares.value = [];
     }
     shares.value = res.portfolio_details.details
   }catch (e){
     useToast().toast({
       title: "Error",
       description: "An error occured while fetching shares",
       duration: 5000,
       icon: "lucide:x",
     });
   }
  }

  await fetchShares(id);

  watch(refresh, async () => {
    await fetchShares(id);
    refresh.value = false;
  })




</script>

<template>
  <div class="overflow-y-auto">
    <div class="grid grid-cols-1 gap-5 md:flex md:items-center md:justify-between">
      <div class="flex flex-col">
        <h1 class="font-semibold">Részvények</h1>
        <p class="text-sm text-muted-foreground">
          A porfolióban található részvények listája
        </p>
      </div>
      <div>
        <AddStock v-model="refresh"/>
      </div>
    </div>

    <div class="mt-10 h-[500px] overflow-auto">
      <UiTable>
        <UiTableHeader>
          <UiTableRow>
            <UiTableHead class="sticky top-0 z-10 bg-background/90 pl-0 font-semibold text-foreground backdrop-blur">Szimbólum</UiTableHead>
            <UiTableHead class="sticky top-0 z-10 bg-background/90 pl-0 font-semibold text-foreground backdrop-blur lg:table-cell">Vásárlási ár/db</UiTableHead>
            <UiTableHead class="sticky top-0 z-10 bg-background/90 pl-0 font-semibold text-foreground backdrop-blur md:table-cell">Menyiség</UiTableHead>
            <UiTableHead class="sticky top-0 z-10 bg-background/90 pl-0 font-semibold text-foreground backdrop-blur md:table-cell">Hozam</UiTableHead>
            <UiTableHead class="sticky top-0 z-10 bg-background/90 pl-0 font-semibold text-foreground backdrop-blur">Jelenlegi ár</UiTableHead>
            <UiTableHead class="sticky top-0 z-10 bg-background/90 pl-0 font-semibold text-foreground backdrop-blur">Jelenlegi érték</UiTableHead>
            <UiTableHead class="sticky top-0 z-10 bg-background/90 pl-0 font-semibold text-foreground backdrop-blur">Művelet</UiTableHead>
          </UiTableRow>
        </UiTableHeader>
        <UiTableBody v-if="shares">
          <template  v-for="share in shares" :key="share.id">
            <UiTableRow>
              <UiTableCell class="pl-0">
                <div class="flex flex-col">
                  <p class="font-medium">{{ share.share_id }}</p>
                </div>
              </UiTableCell>
              <UiTableCell class="pl-0 text-muted-foreground lg:table-cell">{{share.cost_value }}</UiTableCell>
              <UiTableCell class="pl-0 text-muted-foreground md:table-cell">{{share.quantity }}</UiTableCell>
              <UiTableCell class="pl-0 text-muted-foreground md:table-cell font-semibold" :class="share.change_percentage > 0 ? 'text-green-500' : 'text-red-500'">{{share.change_percentage.toFixed(1) }}%</UiTableCell>
              <UiTableCell class="pl-0 text-muted-foreground md:table-cell">{{share.current_price.toFixed(2) }}</UiTableCell>
              <UiTableCell class="pl-0 text-muted-foreground md:table-cell">{{ (share.quantity * share.current_price).toFixed(2) }}</UiTableCell>

              <UiTableCell class="pl-0 text-right">
                <DeleteShare v-model="refresh" :shareId="share.id"/>
              </UiTableCell>
            </UiTableRow>
          </template>
        </UiTableBody>
      </UiTable>
    </div>
  </div>
</template>


