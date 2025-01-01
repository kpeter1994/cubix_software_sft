<script lang="ts" setup>

  const dialog = ref(false);
  const portfolioStore = usePortfolioStore();


  const form = reactive({
    name: "",
    description: "",
  });

  const submit = async () => {
    await portfolioStore.createPortfolio(form.name, form.description);
    dialog.value = false;
    form.name = "";
    form.description = "";
  };

  const closeDialog = (save: boolean) => {
    useToast().toast({
      title: save ? "Profile updated" : "Changes discarded",
      description: `Your changes has been ${save ? "saved" : "discarded"}.`,
      duration: 5000,
      icon: save ? "lucide:check" : "lucide:x",
    });
    dialog.value = false;
  };
</script>

<template>
  <div>
    <UiDialog v-model:open="dialog">

      <UiDialogTrigger as-child>
        <UiButton class="mt-4 w-full"><Icon class="size-4" name="ant-design:plus-circle-filled" />Új porfolió</UiButton>
      </UiDialogTrigger>

      <UiDialogContent
        class="sm:max-w-[425px]"
        title="Új porfolió létrehozása"
        description="Itt adhatsz meg új portfólió adatokat. Kattints a mentés gombra a változtatások elmentéséhez."
      >
        <template #content>
          <div class="grid gap-4 py-4">
            <div class="grid grid-cols-4 items-center gap-4">
              <UiLabel for="name" class="text-right"> Portfólió név </UiLabel>
              <UiInput id="name" v-model="form.name" class="col-span-3" />
            </div>
            <div class="grid grid-cols-4 items-center gap-4">
              <UiLabel for="username" class="text-right"> Leírás </UiLabel>
              <UiInput id="username" v-model="form.description" class="col-span-3" />
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
            <UiButton type="submit" @click="submit()">Mentés</UiButton>
          </UiDialogFooter>
        </template>
      </UiDialogContent>
    </UiDialog>
  </div>
</template>

<style scoped></style>
