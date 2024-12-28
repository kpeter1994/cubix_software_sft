import { defineStore } from 'pinia'

export const useStockStore = defineStore('stock',() => {

  const stock : any = ref(null)

  const setStock = async (name: string) => {
    stock.value = name
  }

  return{
   stock,
    setStock
  }

});