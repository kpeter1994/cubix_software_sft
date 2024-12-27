export default defineNuxtPlugin((nuxtApp) => {
  const authStore = useAuthStore();
  authStore.init();
})
