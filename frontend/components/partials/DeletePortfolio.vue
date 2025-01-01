<script lang="ts" setup>

  const portfolioStore = usePortfolioStore();
  const route : any = useRoute()
  const showMessage = (message: string) => {
    useSonner(message);
  };

  const deletePortfolio = async () => {
    await portfolioStore.deletePortfolio(route.params.id)
    useSonner.success("Portfolio törlése sikeres");
    await navigateTo("/", { replace: true });
  };

  const model = ref(false);
</script>


<template>
  <div class="flex">
    <UiAlertDialog v-model:open="model">
      <UiAlertDialogTrigger as-child>
        <UiButton variant="destructive"><Icon class="size-4" name="material-symbols-light:delete-rounded" />Porfolió törlése</UiButton>
      </UiAlertDialogTrigger>
      <UiAlertDialogContent @escape-key-down="showMessage('Escape key pressed')">
        <UiAlertDialogHeader>
          <UiAlertDialogTitle>Portfólió törlése</UiAlertDialogTitle>
          <UiAlertDialogDescription>
            Ez a művelet nem vonható vissza. A portfólió véglegesen törlődik, és az adatai eltávolításra kerülnek a szerverünkről.
          </UiAlertDialogDescription>
        </UiAlertDialogHeader>
        <UiAlertDialogFooter>
          <UiAlertDialogCancel text="Mégsem" @click="showMessage('Action cancelled')" />
          <UiAlertDialogAction text="Folytatás" @click="deletePortfolio()" />
        </UiAlertDialogFooter>
      </UiAlertDialogContent>
    </UiAlertDialog>
  </div>
</template>

