<script lang="ts" setup>
  import AddStock from "~/components/partials/AddStock.vue";

  const portfolioStore = usePortfolioStore();
  const route : any = useRoute()
  const shares : any = ref(null);
  const id : number = Number(route.params.id);
  const refresh = ref(false);

  const fetchShares = async (id: number) =>{
    const res : any = await portfolioStore.getSharesForPortfolio(id);
    shares.value = res.shares
  }

  await fetchShares(id);

  watch(refresh, async () => {
    await fetchShares(id);
    refresh.value = false;
  });


</script>

<template>
  <div class="overflow-y-auto">
    <div class="grid grid-cols-1 gap-5 md:flex md:items-center md:justify-between">
      <div class="flex flex-col">
        <h1 class="font-semibold">Users</h1>
        <p class="text-sm text-muted-foreground">
          A list of all the users in your account including their name, title, email and role.
        </p>
      </div>
      <div>
        <AddStock v-model="refresh"/>
      </div>
    </div>

    <div class="mt-10 overflow-auto">
      <UiTable>
        <UiTableHeader>
          <UiTableRow>
            <UiTableHead
              class="sticky top-0 z-10 bg-background/90 pl-0 font-semibold text-foreground backdrop-blur"
            >Szimbólum</UiTableHead
            >
            <UiTableHead
              class="sticky top-0 z-10 hidden bg-background/90 pl-0 font-semibold text-foreground backdrop-blur lg:table-cell"
            >Vásárlási ár/db</UiTableHead
            >
            <UiTableHead
              class="sticky top-0 z-10 hidden bg-background/90 pl-0 font-semibold text-foreground backdrop-blur md:table-cell"
            >Menyiség</UiTableHead
            >
            <UiTableHead
              class="sticky top-0 z-10 hidden bg-background/90 pl-0 font-semibold text-foreground backdrop-blur md:table-cell"
            >Hozam</UiTableHead
            >
            <UiTableHead
              class="sticky top-0 z-10 bg-background/90 pl-0 font-semibold text-foreground backdrop-blur"
            >Jelenlegi érték</UiTableHead
            >
            <UiTableHead class="sticky top-0 z-10 bg-background/90 pl-0 backdrop-blur">
              <span class="sr-only">Actions</span>
            </UiTableHead>
          </UiTableRow>
        </UiTableHeader>
        <UiTableBody>
          <template v-for="share in shares" :key="share.id">
            <UiTableRow>
              <UiTableCell class="pl-0">
                <div class="flex flex-col">
                  <p class="font-medium">{{ share.share_id }}</p>
                </div>
              </UiTableCell>
              <UiTableCell class="hidden pl-0 text-muted-foreground lg:table-cell">{{
                  share.cost_value
                }}</UiTableCell>
              <UiTableCell class="hidden pl-0 text-muted-foreground md:table-cell">{{
                  share.quantity
                }}</UiTableCell>
              <UiTableCell class="pl-0 text-muted-foreground">{{ share.role }}</UiTableCell>
              <UiTableCell class="pl-0 text-right">
                <UiButton size="sm" variant="linkHover2">Edit</UiButton>
              </UiTableCell>
            </UiTableRow>
          </template>
        </UiTableBody>
      </UiTable>
    </div>
  </div>
</template>


