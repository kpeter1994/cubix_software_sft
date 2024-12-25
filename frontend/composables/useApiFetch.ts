
export const useApiFetch = async (path: string, options: any = {}) => {

  const token = localStorage.getItem('authToken');

  const defaultHeaders = {
    baseURL: useRuntimeConfig().public.backendUrl,
    headers: {
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    ...options,
  };

  return $fetch(path, defaultHeaders);

}
