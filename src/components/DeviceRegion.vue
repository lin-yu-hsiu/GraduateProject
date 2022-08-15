<template>
  <n-card hoverable closable style="background-color: #ffffff; border-radius: 30px;
  height: 600px; width: 900px; margin: 0 auto;">
    <n-scrollbar style="max-height: 500px; background-color: #ffffff;">
      <div style="position: relative;">
        <div v-if="!emptyflag" class="detailFrameTitle d-flex justify-content-evenly align-items-center mx-3 pb-4">
          <div style="width: 100px; background-color: #ffffff; height: 35px;"></div>
          <div class="subtitle">地點</div>
          <div class="subtitle">電量</div>
          <div class="subtitle" style="width: 150px">訊息</div>
          <button class="openBtn" name="OpenAllDevice" v-if="this.shutdown" @click="alldevicestatusChange">一鍵開機</button>
          <button class="closeBtn" name="CloseAllDevice" v-else @click="alldevicestatusChange">一鍵關機</button>
          <div class="subtitle" style="width: 150px">備註</div>
        </div>
        <div v-else class="text-center m-auto"
          style="font-weight: bold; font-size: 24px;color: rgba(0, 0, 0, 20%); margin: auto;">
          目前此區域無任何裝置
        </div>
        <div v-if="!emptyflag">
          <DeviceInfo @ifEmpty="ifEmpty_DeviceRegion" v-for="item in devices" :key="item.id" :device="item">
          </DeviceInfo>
        </div>
      </div>
    </n-scrollbar>
  </n-card>
</template>

<script>
import axios from 'axios'
import { defineComponent, inject } from "vue";
import DeviceInfo from './DeviceInfo.vue'


export default defineComponent({
  setup() {
    const reload = inject('reload')
    const update = () => {
      reload()
    }
    return {
      update,
    }
  },
  data() {
    return {
      devices: [],
      alldevices: [],
      shutdown: '',
      mapNum: this.passMapNum,
      emptyflag: '',
    }
  },
  props: {
    passMapNum: {
      type: Number,
      required: true
    }
  },
  watch: {
    passMapNum(newVal) {
      this.mapNum = newVal
    }
  },
  components: {
    DeviceInfo
  },
  methods: {
    async handleAPI(mapNum) {
      const API = this.$store.state.api + '/deviceInfo/'
      await axios({
        method: 'get',
        baseURL: API,
        url: mapNum.toString(),
        headers: { 'Content-Type': 'application/json' },
      })
        .then((response) => this.devices = response.data)
        .catch((error) => console.log(error))
      // 偵測是否有裝置
      for (let i = 0; i < this.devices.length; i++) {
        if (this.devices[i].Status == false) {
          this.shutdown = true
        }
        else this.shutdown = false
      }

      if (this.devices.length == 0) {
        this.emptyflag = true   // 一開始此區域即無裝置
        this.$emit('emptyregion', this.emptyflag)
      }
    },
    async alldevicestatusChange() {
      const body = {
        // 傳其中一個device的MapNum跟Status就好
        'MapNum': this.devices[0].MapNum,
        'Status': this.shutdown
      }
      const json = JSON.stringify(body);
      console.log(json)
      let res = []
      await axios.post(this.$store.state.api + '/switchBLE', json, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((response) => res = response.data)
        .catch((err) => console.log(err))
      console.log(res)
      this.handleAPI(this.mapNum)
    },
    ifEmpty_DeviceRegion() {
      this.handleAPI(this.mapNum)
      console.log(this.devices.length)
      if (this.devices.length == 1) {
        this.emptyflag = true   // 刪除裝置後此區域無裝置
        this.$emit('ifEmpty', this.emptyflag)
      }
    }
  },
  mounted() {
    this.handleAPI(this.mapNum)
  }
})
</script>

<style scoped>
.detailFrameTitle {
  position: sticky;
  top: 0;
  z-index: 1;
  background-color: #ffffff;
}

.subtitle {
  width: 100px;
  height: 35px;
  background-color: rgba(201, 201, 201, 80%);
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 25%);
  font-weight: bold;
  text-align: center;
  font-size: 20px;
  line-height: 2;
}

.openBtn {
  width: 100px;
  height: 35px;
  background-color: rgba(201, 201, 201, 80%);
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 25%);
  font-weight: 550;
  text-align: center;
  font-size: 20px;
  outline: none;
  border: none;
  line-height: 1.9;
  transition: all 100ms ease;
}

.openBtn:hover {
  /* background-color: rgba(0, 0, 0, 75%); */
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 15%) inset, 0 -1px 4px 0 rgba(0, 0, 0, 15%) inset;
  color: #0FA958;
  border-radius: 5px;
}

.closeBtn {
  width: 100px;
  height: 35px;
  background-color: rgba(201, 201, 201, 80%);
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 25%);
  font-weight: 550;
  text-align: center;
  font-size: 20px;
  outline: none;
  border: none;
  line-height: 1.9;
  transition: all 100ms ease;
}

.closeBtn:hover {
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 15%) inset, 0 -1px 4px 0 rgba(0, 0, 0, 15%) inset;
  color: #fd2d2d;
  border-radius: 5px;
}
</style>