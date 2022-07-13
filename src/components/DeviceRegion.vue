<template>
  <n-card hoverable closable style="background-color: #ffffff; border-radius: 30px;
  height: 600px; width: 800px;">
    <n-scrollbar style="max-height: 500px; background-color: #ffffff;">
      <div style="position: relative;">
        <div class="detailFrameTitle d-flex justify-content-evenly align-items-center mx-3">
          <div style="width: 100px; background-color: #ffffff; height: 35px;"></div>
          <div class="subtitle">地點</div>
          <div class="subtitle">電量</div>
          <div class="subtitle" style="width: 150px">訊息</div>
          <div class="subtitle">開 / 關機</div>
        </div>
        <DeviceInfo></DeviceInfo>
        <DeviceInfo></DeviceInfo>
        <DeviceInfo></DeviceInfo>
        <DeviceInfo></DeviceInfo>
        <DeviceInfo></DeviceInfo>
        <DeviceInfo></DeviceInfo>
        <DeviceInfo></DeviceInfo>
        <DeviceInfo></DeviceInfo>
        <DeviceInfo></DeviceInfo>
        <DeviceInfo></DeviceInfo>
        <DeviceInfo></DeviceInfo>
      </div>
    </n-scrollbar>
  </n-card>
</template>

<script>
import { defineComponent } from 'vue'
import DeviceInfo from './DeviceInfo.vue'


export default defineComponent({
  setup() {

  },
  components: {
    DeviceInfo
  },
  methods: {

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
</style>