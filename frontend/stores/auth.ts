import { defineStore } from 'pinia'


export const useAuthStore = defineStore('auth',() => {
  const user = ref(null)
  const token = ref<string | null>(null); // Az auth token
  const isLoading = ref(false);
  const isLogedIn = computed(() => !!user.value);

  const init = async () => {
    const savedToken = localStorage.getItem('authToken');
    if (savedToken) {
      token.value = savedToken;
      await verifyToken(savedToken);
    }
  };

  const verifyToken = async (savedToken: string) => {
    try {
      const response : any = await $fetch('/verification',{
        baseURL: useRuntimeConfig().public.backendUrl,
        headers: { Authorization: `Bearer ${token.value}` }
      })
      user.value = response.user;
    } catch (error) {
      console.error("Token verification failed:", error);
      localStorage.removeItem('authToken');
      localStorage.removeItem('user');
    }
  }

  const login = async (username: string, password: string) => {

    isLoading.value = true;

    try {
      const response : any = await $fetch('/login',{
        baseURL: useRuntimeConfig().public.backendUrl,
        method: 'POST',
        body: { username, password },
      })

      token.value = response.token;

      if (token.value) {
        localStorage.setItem('authToken', token.value);
        await verifyToken(token.value)
      }

    } catch (error) {
      console.error(error)
    } finally {
      isLoading.value = false;
    }

  }

  const logout =  () => {
    user.value = null;
    token.value = null;
    localStorage.removeItem('authToken');
    localStorage.removeItem('user');
  }



  return{
    user,
    token,
    isLoading,
    isLogedIn,
    login,
    init,
    logout
  }

});