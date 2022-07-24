import { createStore } from 'vuex'

export default createStore({
  state: {
    currvenue: false,
    currentvenue: '(需先切換場館)',
    currentarea: null,
    api: 'http://192.168.0.103:5000/'
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
