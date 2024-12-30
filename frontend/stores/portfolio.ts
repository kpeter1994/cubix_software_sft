import { defineStore } from 'pinia'
import { useApiFetch } from "~/composables/useApiFetch";



export const usePortfolioStore = defineStore('portfolio',() => {

  const allPortfolio: any = ref([]);
  const portfolio : any = reactive({
    name: '',
    description: '',
  })

  const getAllPortfolios = async () => {
    return allPortfolio.value = await useApiFetch('/stock/get-user-portfolios',{'method': 'GET'});
  }

 const createPortfolio = async (name: string, description: string) => {
    portfolio.name = name;
    portfolio.description = description;
    await useApiFetch('/stock/create-portfolio',{'method': 'POST', 'body': JSON.stringify(portfolio)});
    await getAllPortfolios();
 }

 const addSharesToPortfolio = async (portfolio_id: string, share_data: object) => {
    return await useApiFetch('/stock/add-shares-to-portfolio',{'method': 'POST', 'body': JSON.stringify({portfolio_id, share_data})});
 }

 const getSharesForPortfolio = async (portfolio_id: number) => {
   return await useApiFetch(`/stock/get-portfolio-details?portfolio_id=${portfolio_id}`,{'method': 'GET'});
 }


  return{
    portfolio,
    allPortfolio,
    getAllPortfolios,
    createPortfolio,
    addSharesToPortfolio,
    getSharesForPortfolio,
  }

});