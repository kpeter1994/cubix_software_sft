import { useAuthStore } from "~/stores/auth";

export default defineNuxtRouteMiddleware(async (to, from) => {

   const { isLogedIn } = storeToRefs(useAuthStore())


    if (isLogedIn.value == true) {
        return await navigateTo('/')
    }

})
