<script lang="ts" setup>
  const props = defineProps<{ shareId: number }>();

  const refresh = defineModel<boolean>()
  const portfolioStore = usePortfolioStore();
  const route : any = useRoute()
  const showMessage = (message: string) => {
    useSonner(message);
  };

  const deleteShare = async () => {
    await portfolioStore.deleteShareFromPortfolio(route.params.id, props.shareId)
    useSonner.success("Részvény törölve a porfolióból");
    refresh.value = true;
  };

  const model = ref(false);
</script>

<template>
  <div>
    <UiAlertDialog v-model:open="model">
      <UiAlertDialogTrigger as-child>
        <UiButton size="sm" variant="destructive"><Icon class="size-4" name="material-symbols-light:delete-rounded" /></UiButton>
      </UiAlertDialogTrigger>
      <UiAlertDialogContent @escape-key-down="showMessage('Escape key pressed')">
        <UiAlertDialogHeader>
          <UiAlertDialogTitle>Részvény törlése a porfolióbol</UiAlertDialogTitle>
          <UiAlertDialogDescription>
            Ez a művelet nem vonható vissza. A portfólió véglegesen törlődik, és az adatai eltávolításra kerülnek a szerverünkről.
          </UiAlertDialogDescription>
        </UiAlertDialogHeader>
        <UiAlertDialogFooter>
          <UiAlertDialogCancel text="Mégsem" @click="showMessage('Action cancelled')" />
          <UiAlertDialogAction text="Folytatás" @click="deleteShare()" />
        </UiAlertDialogFooter>
      </UiAlertDialogContent>
    </UiAlertDialog>
  </div>
</template>

<style scoped></style>
