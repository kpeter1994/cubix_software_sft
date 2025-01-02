<script setup lang="ts">
const authStore = useAuthStore();
const config = useRuntimeConfig();
console.log(config.public.backendUrl);
const loading = computed(() =>{
  return authStore.loading;
})
</script>
<template>
    <NuxtLoadingIndicator/>
    <NuxtLayout>
      <div v-if="loading">loading..</div>
      <NuxtPage v-if="!loading"></NuxtPage>
    </NuxtLayout>
    <UiVueSonner />
</template>
