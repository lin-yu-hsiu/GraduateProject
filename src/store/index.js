import { createStore } from 'vuex'

export default createStore({
  state: {
    currentvenue: '(需先切換場館)',
    currentarea: null,
  },
  getters: {

  },
  mutations: {
    switchRegion(state, curr) {
      state.currentvenue = curr;
      console.log(curr)
    },
    listRegion() {

    },
    countVenue(state) {
      state.countvenue += 1;
    }
  },
  actions: {
    switch_region(context, curr) {
      context.commit("switchRegion", curr)
    }
  },
  modules: {
  }
})
