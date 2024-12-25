import { fa } from "cronstrue/dist/i18n/locales/fa";

export default defineNuxtRouteMiddleware(async (to, from) => {
  const { isLogedIn } = storeToRefs(useAuthStore())

  if (isLogedIn.value == false) {
    if (to.path !== '/login' && to.path !== '/register') {
      return await navigateTo('/login')
    }
  }


})