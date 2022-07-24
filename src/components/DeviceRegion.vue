<template>
  <n-card hoverable closable style="background-color: #ffffff; border-radius: 30px;
  height: 600px; width: 900px;">
    <n-scrollbar style="max-height: 500px; background-color: #ffffff;">
      <div style="position: relative;">
        <div class="detailFrameTitle d-flex justify-content-evenly align-items-center mx-3 py-3">
          <div style="width: 100px; background-color: #ffffff; height: 35px;"></div>
          <div class="subtitle">地點</div>
          <div class="subtitle">電量</div>
          <div class="subtitle" style="width: 150px">訊息</div>
          <button class="openBtn" name="OpenAllDevice" v-if="this.shutdown" @click="alldevicestatusChange">一鍵開機</button>
          <button class="closeBtn" name="CloseAllDevice" v-else @click="alldevicestatusChange">一鍵關機</button>
          <div class="subtitle" style="width: 150px">備註</div>
        </div>
        <DeviceInfo v-for="item in devices" :key="item.id" :device="item"></DeviceInfo>
      </div>
    </n-scrollbar>
  </n-card>
</template>

<script>
import axios from 'axios'
import { defineComponent } from "vue";
import DeviceInfo from './DeviceInfo.vue'


export default defineComponent({
  data() {
    return {
      devices: [],
      alldevices: [],
      shutdown: '',
      mapNum: this.passMapNum,
    }
  },
  props: {
    passMapNum: {
      required: true
    }
  },
  components: {
    DeviceInfo
  },
  methods: {
    async handleAPI(mapNum) {
      const API = 'http://192.168.0.103:5000/deviceInfo/'
      await axios({
        method: 'get',
        baseURL: API,
        url: mapNum.toString(),
        'Content-Type': 'application/json',
      })
        .then((response) => this.devices = response.data)
        .catch((error) => console.log(error))
      for (let i = 0; i < this.devices.length; i++) {
        if (this.devices[i].Status == false) {
          this.shutdown = true
        }
        else this.shutdown = false
      }
    },
    async alldevicestatusChange() {

      console.log(this.devices)
      const switchBLEAPI = 'http://192.168.0.103:5000/switchBLE'
      // let res = ''
      const body = {
        // 傳其中一個device的MapNum跟Status就好
        'MapNum': this.devices[0].MapNum,
        'Status': this.shutdown
      }
      const json = JSON.stringify(body);
      console.log(json)
      const res = await axios.post(switchBLEAPI, json, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      console.log(res)
      this.handleAPI(this.mapNum)
    },
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