<script lang="ts" setup>
  import dayjs from 'dayjs';
  import { useStockStore } from "~/stores/stock";

  const portfolioStore = usePortfolioStore();
  const dialog = ref(false);
  const route : any = useRoute()

  const stockStore = useStockStore()
  const selectedShare = computed(() => stockStore.stock);
  const refresh = defineModel<boolean>();

  const closeDialog = (save: boolean) => {
    useToast().toast({
      title: save ? "Profile updated" : "Changes discarded",
      description: `Your changes has been ${save ? "saved" : "discarded"}.`,
      duration: 5000,
      icon: save ? "lucide:check" : "lucide:x",
    });
    dialog.value = false;
  };
  const id : number = Number(route.params.id);

  const stock = reactive({
    share_id: selectedShare,
    price: 0,
    quantity: 0,
  });

  const submit = async () => {
    const today = new Date();

    await portfolioStore.addSharesToPortfolio(id, [
      {
      share_id: stock.share_id,
      cost_value: stock.price,
      quantity: stock.quantity,
      date: dayjs(today).format("YYYY-MM-DD"),
    }
    ]);
    dialog.value = false;
    refresh.value = true;
  };
</script>

<template>
  <div class="flex w-full items-center justify-center">
    <UiDialog v-model:open="dialog">
      <UiDialogTrigger as-child>
        <UiButton>Résszvény hozzáadása</UiButton>
      </UiDialogTrigger>

      <UiDialogContent
        class="sm:max-w-[425px]"
        title="Résszvény hozzáadása"
        description="Addj hozzá egy új részvényt a portfóliódhoz."
      >
        <template #content>
          <div class="grid gap-4 py-4">
            <div class="grid grid-cols-4 items-center gap-4">
              <UiLabel for="name" class="text-right"> Részvény </UiLabel>
              <UiInput id="name" v-model="stock.share_id" class="col-span-3" />
            </div>
            <div class="grid grid-cols-4 items-center gap-4">
              <UiLabel for="username" class="text-right"> Ár </UiLabel>
              <UiInput id="username" type="number" v-model="stock.price" class="col-span-3" />
            </div>
            <div class="grid grid-cols-4 items-center gap-4">
              <UiLabel for="username" class="text-right"> Mennyiség </UiLabel>
              <UiInput id="username" type="number" v-model="stock.quantity" class="col-span-3" />
            </div>
          </div>
        </template>
        <template #footer>
          <UiDialogFooter>
            <UiButton
              variant="outline"
              type="button"
              class="mt-2 sm:mt-0"
              @click="closeDialog(false)"
            >Cancel</UiButton
            >
            <UiButton type="submit" @click="submit()">Save</UiButton>
          </UiDialogFooter>
        </template>
      </UiDialogContent>
    </UiDialog>
  </div>
</template>


