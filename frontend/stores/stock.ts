import { defineStore } from 'pinia'
import { useApiFetch } from "~/composables/useApiFetch";

export const useStockStore = defineStore('stock',() => {

  const stock : any = ref(null)

  const setStock = async (name: string) => {
    stock.value = name
  }

  const getShareActualData = async (symbol: string) => {
    return await useApiFetch(`/stock/current-price?stock_symbol=${symbol}`,{'method': 'GET'});
  }

  return{
   stock,
    setStock,
    getShareActualData
  }

});