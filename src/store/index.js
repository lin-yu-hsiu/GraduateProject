import { createStore } from 'vuex'

export default createStore({
  state: {
    step: '',
    currvenue: false,
    currentvenue: '(需先切換場館)',
    api: 'http://192.168.0.103:5000',
    currentUser: '',
    venueEditMode: false,
    allvenues: [],
    deviceEditMode: false,
    regionAddName: ''
  },
  getters: {
  },
  mutations: {
    switchRegion(state, curr) {
      state.currentvenue = curr;
      state.currvenue = true
      state.step = 'switch'
    },
    addRegion(state) {
      state.step = 'addregion'
    },
    addDevice(state) {
      state.step = 'addDevice'
    },
  },
  actions: {
  },
  modules: {
  }
})
