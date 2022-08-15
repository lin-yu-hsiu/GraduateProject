<template>
  <!-- :class="[regionStatus ? noError : Error]" -->
  <div class="regionList m-3"
    :class="[{ 'mistake': regionStatus == 'error' }, { 'no_mistake': regionStatus == 'good' }, { 'normal': regionStatus == 'normal' }]">
    <div class="d-flex justify-content-around align-items-center w-100">
      <div style="font-weight: bold; align-self: start; font-size: 26px;">{{ region.Area }}</div>
      <button class="detailBtn p-0" v-if="this.$store.state.deviceEditMode" @click="sendToRemoveRegion()"
        @mouseover="icon = remove_hover" @mouseleave="icon = remove">
        <img :src="icon" style="width: 30px; height: 35px">
      </button>
    </div>
    <button v-if="regionStatus == 'error' && !this.$store.state.deviceEditMode" class="viewDetail" @click="open = true">
      <img :src="fordetail">
      查看裝置問題
    </button>
    <button v-if="regionStatus == 'good' && !this.$store.state.deviceEditMode" class="viewDevice" @click="open = true">
      <img :src="devicegood">
      裝置一切正常
    </button>
    <button v-if="regionStatus == 'normal' && !this.$store.state.deviceEditMode" class="viewNone"
      style="cursor: not-allowed;">
      <img :src="none" style="width: 50px; height: 50px">
      此區域無裝置
    </button>
    <router-link :to="{ name: 'adddevice' }">
      <button v-if="this.$store.state.deviceEditMode" class="AddDevice"
        @click="this.$store.state.regionAddName = region.Area">
        新增裝置
      </button>
    </router-link>
  </div>
  <DeviceRegion @ifEmpty="ifEmpty_ViewRegion" :passMapNum="region.Number" v-if="open" @close="open = false" style="position: absolute; 
        top: 0;             
        bottom: 0;           
        left: 0;        
        right: 0;
        margin: auto;  ">
  </DeviceRegion>
</template>

<script>
import axios from 'axios'
import DeviceRegion from './DeviceRegion.vue'
import { inject } from "vue";
import detail from '../assets/pic/fordetail_red.png'
import good from '../assets/pic/good_green.png'
import none from '../assets/pic/eyes_none.png'
import remove from '../assets/pic/trash.png'
import remove_hover from '../assets/pic/trash_hover.png'

export default {
  setup() {
    const reload = inject('reload')
    const update = () => {
      reload()
    }
    return {
      update
    }
  },
  components: {
    DeviceRegion
  },
  props: {
    region: {
      required: true
    }
  },
  watch: {
    region(newVal) {
      this.regions = newVal
    },
    regionStatus(newVal) {
      this.regionStatus = newVal
    }
  },
  data() {
    return {
      icon: remove,
      remove: remove,
      remove_hover: remove_hover,
      fordetail: detail,
      devicegood: good,
      none: none,

      regions: this.region,

      open: false,
      regionStatus: 'good',
    }
  },
  methods: {
    async viewRegion(mapNum) {
      const API = this.$store.state.api + '/deviceInfo/'
      await axios({
        method: 'get',
        baseURL: API,
        url: mapNum.toString(),
        headers: { 'Content-Type': 'application/json' },
      })
        .then((response) => this.devices = response.data)
        .catch((error) => console.log(error))

      // 如果此區域已無裝置
      if (this.devices.length == 0) {
        this.regionStatus = 'normal'
      }

      // 尋訪指定區域中是否有裝置狀態異常 (ex:電池沒電)
      for (let i = 0; i < this.devices.length; i++) {
        if (this.devices[i].Battery == '0%') {
          this.regionStatus = 'error'
        }
      }

    },
    ifEmpty_ViewRegion(value) {
      if (value == true) {
        this.regionStatus = 'normal'
      }
      this.$emit('ifEmpty')
    },
    async sendToRemoveRegion() {
      let body = {
        'MapNum': this.regions.Number,
      }
      const json = JSON.stringify(body)
      await axios({
        method: 'post',
        url: this.$store.state.api + '/deleteArea',
        headers: { 'Content-Type': 'application/json' },
        data: json
      }).then((response) => response = response.data)
        .catch((err) => { console.error(err) })
      this.$emit('_reDisplay')
    }
  },
  mounted() {
    this.viewRegion(this.regions.Number)
  },
}
</script>

<style scoped>
.regionList {
  width: 270px;
  height: 150px;
  background: linear-gradient(to bottom, #ffffff 0%, rgba(142, 142, 142, 50%) 100%);
  box-shadow: 0 10px 10px 0 rgba(0, 0, 0, 25%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  border-radius: 20px;
  padding: 20px;
}

.regionList:hover {
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 5%) inset;
}

.AddDevice {
  font-weight: bold;
  font-size: 18px;
  border-radius: 5px;
  box-shadow: 0 0 5px 5px rgba(0, 0, 0, 0.1);
  width: 130px;
  padding: 5px 5px;
  border: none;
  outline: none;
  transition: all 0.2s ease;
}

.AddDevice:hover {
  /* background-color: rgba(215, 215, 215, 0.8); */
  color: rgb(0, 200, 83);
  width: 155px;
}

.detailBtn {
  background-color: transparent;
  border: none;
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

.viewNone {
  background-color: #363636;
  color: #D9D9D9;
  font-weight: bold;
  font-size: 24px;
  width: 220px;
  height: 60px;
  border-radius: 10px;
  padding: 4px 8px;
  border: none;
}

.viewDetail:hover,
.viewDevice:hover,
.viewNone:hover {
  background-color: #2c2c2c;
}

.no_mistake {
  border: ridge 3px #0FA958;
}

.mistake {
  border: ridge 3px #fd2d2d;
}

.normal {
  border: ridge 3px #bebebe;
}
</style>
