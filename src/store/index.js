import { createStore } from 'vuex'

export default createStore({
  state: {
    currvenue: false,
    currentvenue: '(需先切換場館)',
    api: 'http://192.168.0.101:5000'
  },
  getters: {
  },
  mutations: {
    switchRegion(state, curr) {
      state.currentvenue = curr;
      state.currvenue = true
      console.log(curr)
    },
  },
  actions: {
  },
  modules: {
  }
})
