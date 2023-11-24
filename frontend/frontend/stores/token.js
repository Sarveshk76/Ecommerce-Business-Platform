import { defineStore } from 'pinia'

export const useTokenStore = defineStore('token', {
  state: () => {
    return { token: "" }
  },
  getters: {
    getToken() {
      return this.token
    },
  },
  
  actions: {
    setToken(token) {
      this.token = token
    },
    loginCustomer(){

    },
  },
})