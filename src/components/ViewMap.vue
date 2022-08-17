<template>
  <n-card hoverable closable style="background-color: rgba(233, 229, 217, 1); border-radius: 20px;
  height: 700px; width: 700px; margin: 0 auto;">
    <div style="margin: 0 auto;position: relative;height: 600px; width: 600px;">
      <img style="border-radius: 5px; width: 100%; height: 100%;"
        :src="'../../images/' + this.$store.state.currentvenue + '/' + this.$store.state.currentvenue + '_' + this.$store.state.openMapName + '.jpg'"
        alt="">
      <div v-for="item in currentdevice" :key="item">
        <n-tooltip trigger="hover">
          <template #trigger>
            <img :src="already_locate" :style="styleobj" v-on="setPosition(item.x, item.y)">
          </template>
          地點 : {{ item.place }}
          <br>
          電量 : {{ item.battery }}
        </n-tooltip>
      </div>
    </div>
  </n-card>
</template>

<script>
import axios from 'axios'
import { reactive } from 'vue'
import already_locate from '../assets/pic/already_locate.png'

export default {
  setup() {
    let styleobj = reactive({
      width: '20px',
      height: '20px',
      position: 'absolute',
      top: '',
      left: ''
    });
    const setPosition = (x, y) => {
      styleobj.top = y + 'px'
      styleobj.left = x + 'px'
    }
    return {
      setPosition,
      styleobj,
    }
  },
  data() {
    return {
      currentdevice: [],
      already_locate: already_locate,
    }
  },
  methods: {
    async fetchPicInfo() {
      let devices
      await axios({
        method: 'get',
        baseURL: this.$store.state.api + '/deviceInfo',
        'Content-Type': 'application/json',
      })
        .then((response) => devices = response.data)
        .catch((err) => { console.error(err) })

      for (let i = 0; i < Object.values(devices).length; i++) {
        if (devices[i].Area === this.$store.state.openMapName) {
          this.currentdevice.push({ 'x': devices[i].Xaxis, 'y': devices[i].Yaxis, 'battery': devices[i].Battery, 'place': devices[i].Place })
        }
      }
      // console.log(this.currentdevice)
    },
  },
  mounted() {
    this.fetchPicInfo()
  }
}
</script>

<style>
</style>