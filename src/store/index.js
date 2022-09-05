import { createStore } from 'vuex'

export default createStore({
  state: {
    step: '',
    currvenue: false,
    currentvenue: '(需先切換場館)',
    api: 'http://192.168.50.236:5000',
    currentUser: '',
    venueEditMode: false,
    allvenues: [],
    deviceEditMode: false,
    regionAddName: '',
    openMapFlag: false,
    openMapName: '',
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
    FAQ(state) {
      state.step = 'faq'
      state.venueEditMode = false
      state.deviceEditMode = false
    },
  },
  actions: {
  },
  modules: {
  }
})
