import { defineStore } from 'pinia'

export const usePortfolioStore = defineStore('portfolio',() => {

  const stock : any = ref(null)

  const setStock = async (name: string) => {
    stock.value = name
  }

  return{
   stock,
    setStock
  }

});