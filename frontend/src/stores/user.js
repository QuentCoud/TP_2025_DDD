import { defineStore } from 'pinia'

export const useUser = defineStore('user', {
  state: () => ({
    currentUser: null
  }),
  actions: {
    setUser(userData) {
      this.currentUser = userData
    },
    clearUser() {
      this.currentUser = null
    }
  },
  getters: {
  }
})