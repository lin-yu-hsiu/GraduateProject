<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column align-items-center p-5 w-100" :class="(locating && no_cursor) ? notlocateCursor : ''"
      style="position: relative">
      <button class="locateBtn mb-3" @click="add_status = true; locating = true;">
        <img :src="locatePic">
      </button>
      <div class="frame">
        <img :src="pic" :class="locating ? canlocateCursor : ''" @click="add_device = true; no_cursor = false">
      </div>
      <AddDeviceInfo style="cursor: default;" v-if="add_status && add_device"
        @close="add_status = false; add_device = false; locating = false"></AddDeviceInfo>
    </div>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue';
import AddDeviceInfo from '@/components/AddDeviceInfo.vue';

import locatePic from '../assets/pic/location.png'
import regionpic2 from '../assets/pic/regionpic2.jpg'

export default {
  components: {
    MenuBar,
    AddDeviceInfo
  },
  data() {
    return {
      locatePic: locatePic,
      pic: regionpic2,
      add_status: false,
      add_device: false,
      locating: false,
      canlocateCursor: 'locateCursor',
      notlocateCursor: 'notlocateCursor',
      normalCursor: 'normalCursor',
      no_cursor: true,
    };
  },
  methods: {
  }
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
  margin: 0 auto;
  padding: 20px 0;
}

.locateCursor {
  cursor: url('../assets/pic/locate_green.png'), pointer;
}

.notlocateCursor {
  cursor: url('../assets/pic/locate.png'), pointer;
}

.normalCursor {
  cursor: default;
}
</style>