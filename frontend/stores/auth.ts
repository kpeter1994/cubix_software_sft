import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth',() => {
  const user = ref(null)
  const token = ref<string | null>(null); // Az auth token
  const isLogedIn = computed(() => !!user.value);
  const loading = ref(true);

  const init = async () => {
    const savedToken = localStorage.getItem('authToken');
    if (savedToken) {
      token.value = savedToken;
      await verifyToken(savedToken);
    }
    loading.value = false;
  };


  const register = async (data: object) => {
    try {
      const response: any = await $fetch('/auth/register', {
        baseURL: useRuntimeConfig().public.backendUrl,
        method: 'POST',
        body: data,
      })

      token.value = response.token;

      if (token.value) {
        localStorage.setItem('authToken', token.value);
        await verifyToken(token.value)
      }

    } catch (error) {
      console.error(error)
    }

  }

  const verifyToken = async (savedToken: string) => {
    try {
      const response : any = await $fetch('/auth/verification',{
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

    try {
      const response : any = await $fetch('/auth/login',{
        baseURL: useRuntimeConfig().public.backendUrl,
        method: 'POST',
        body: { username, password },
      })

      token.value = response.token;

      if (token.value) {
        localStorage.setItem('authToken', token.value);
        await verifyToken(token.value)
      }
      return response;

    } catch (error) {
      console.error(error)
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
    isLogedIn,
    loading,
    login,
    register,
    init,
    logout
  }

});