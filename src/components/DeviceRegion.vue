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
          <button class="openBtn" v-if="!shutdown" @click="Opendevice">一鍵開機</button>
          <button class="closeBtn" v-if="shutdown" @click="Closedevice">一鍵關機</button>
          <div class="subtitle" style="width: 150px">備註</div>
        </div>
        <DeviceInfo v-for="item in devices" :key="item.id" :device="item"></DeviceInfo>
      </div>
    </n-scrollbar>
  </n-card>
</template>

<script>
import { defineComponent } from 'vue'
import DeviceInfo from './DeviceInfo.vue'

const devices = [
  {
    position: '1',
    battery: 'battery100',
    message: '1',
    switch: true,
    ps: '1',
  },
  {
    position: '2',
    battery: 'battery90',
    message: '2',
    switch: false,
    ps: '2',
  },
  {
    position: '3',
    battery: 'battery80',
    message: '3',
    switch: false,
    ps: '3',
  },
  {
    position: '4',
    battery: 'battery60',
    message: '4',
    switch: true,
    ps: '4',
  }
];

export default defineComponent({
  components: {
    DeviceInfo
  },
  data() {
    return {
      devices: devices,
      shutdown: false,
      deviceNum: 4,
    }
  },
  methods: {
    Opendevice() {
      for (let i = 0; i < this.deviceNum; i++) {
        this.devices[i].switch = true
      }
      this.shutdown = true
    },
    Closedevice() {
      for (let i = 0; i < this.deviceNum; i++) {
        this.devices[i].switch = false
      }
      this.shutdown = false
    }
  },
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