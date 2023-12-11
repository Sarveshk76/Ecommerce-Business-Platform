import { defineStore } from 'pinia'


export const useTokenStore = defineStore('token', {
  state: () => {
    return { token: "" }
  },
  getters: {
    getToken() {
      if(process.client) {
      return localStorage.getItem("token")
      }
      return ""
    },
  },
  
  actions: {
    setToken(token) {
      if(process.client) {
      localStorage.setItem("token", token)
      }
      return ""
    },
    loginCustomer(){

    },
  },
})