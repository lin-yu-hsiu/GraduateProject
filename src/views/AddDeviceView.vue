<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column align-items-center p-5 w-100" style="position: relative">
      <button class="locateBtn mb-3">
        <img :src="locatePic">
      </button>
      <div class="frame">
        <img :src="pic">
      </div>
      <AddDeviceInfo></AddDeviceInfo>
    </div>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue';
import AddDeviceInfo from '@/components/AddDeviceInfo.vue';

import locatePic from '../assets/pic/location.png'
import testpic2 from '../assets/pic/2.jpg'

export default {
  components: {
    MenuBar,
    AddDeviceInfo
  },
  data() {
    return {
      locatePic: locatePic,
      pic: testpic2,

    };
  },
};
</script>

<style scoped>
.locateBtn {
  border: none;
  background-color: transparent;
  width: 65px;
  height: 70px;
  border-radius: 15px;
  display: flex;
  justify-content: center;
  align-items: center;
  align-self: flex-start;
}

.locateBtn:focus {
  background-color: rgba(0, 0, 0, 75%);
}

.frame {
  width: 80vw;
  height: 700px;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 25%) inset;
  padding: 8px;
  position: relative;
}

.frame img {
  max-height: 100%;
  max-width: 100%;
  width: auto;
  height: auto;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
}
</style>