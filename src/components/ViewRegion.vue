<template>
  <div class="regionList m-3" :class="[regionStatus ? noError : Error]">
    <div style="font-weight: bold; align-self: start; font-size: 26px;">{{ region.Area }}</div>
    <button v-if="!regionStatus" class="viewDetail" @click="open = true">
      <img :src="fordetail">
      查看裝置問題
    </button>
    <button v-if="regionStatus" class="viewDevice" @click="open = true">
      <img :src="devicegood">
      裝置一切正常
    </button>
  </div>
  <DeviceRegion :passMapNum="region.MapNum" v-if="open" @close="open = false"
    style="position: absolute; top:20vh; left:25vw">
  </DeviceRegion>
</template>

<script>
// import axios from 'axios';
import DeviceRegion from './DeviceRegion.vue'

import detail from '../assets/pic/fordetail_red.png'
import good from '../assets/pic/good_green.png'



export default {
  components: {
    DeviceRegion
  },
  props: {
    region: {
      required: true
    }
  },
  data() {
    return {
      fordetail: detail,
      devicegood: good,

      regions: this.region,

      Error: 'mistake',
      noError: 'no_mistake',
      open: false,
      regionStatus: false,
    }
  },
  methods: {

  },
  mounted() {

  },
}
</script>

<style scoped>
.regionList {
  width: 400px;
  height: 250px;
  background: linear-gradient(to bottom, #ffffff 0%, rgba(142, 142, 142, 50%) 100%);
  box-shadow: 0 10px 10px 0 rgba(0, 0, 0, 25%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  border-radius: 0 0 20px 20px;
  padding: 20px;

}

.regionList:hover {
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 5%) inset;
}

.viewDetail {
  background-color: #363636;
  color: #fd2d2d;
  font-weight: bold;
  font-size: 24px;
  width: 220px;
  height: 60px;
  border-radius: 10px;
  padding: 4px 8px;
  border: none;
}

.viewDevice {
  background-color: #363636;
  color: #0FA958;
  font-weight: bold;
  font-size: 24px;
  width: 220px;
  height: 60px;
  border-radius: 10px;
  padding: 4px 8px;
  border: none;
}

.viewDetail:hover,
.viewDevice:hover {
  background-color: #2c2c2c;
}

.no_mistake {
  border: ridge 3px #0FA958;
}

.mistake {
  border: ridge 3px #fd2d2d;
}
</style>
