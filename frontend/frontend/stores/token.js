import { defineStore } from 'pinia'

export const useTokenStore = defineStore('token', {
  state: () => {
    return { token: "" }
  },
  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    loginCustomer(){

    },
  },
})