import { createStore } from 'vuex'

export default createStore({
  state: {
    step: '',
    currvenue: false,
    currentvenue: '(需先切換場館)',
    api: 'http://192.168.0.102:5000',
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
    },
    switchVenue(state) {
      state.step = 'switch'
      state.venueEditMode = false
      state.deviceEditMode = false
    },
    viewDevice(state) {
      state.step = 'view'
      state.venueEditMode = false
      state.deviceEditMode = false
    },
  },
  actions: {
  },
  modules: {
  }
})
