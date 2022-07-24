import { createStore } from 'vuex'

export default createStore({
  state: {
    currvenue: false,
    currentvenue: '(需先切換場館)',
    currentarea: null,
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
