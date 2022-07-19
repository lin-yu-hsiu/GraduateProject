<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column align-items-center p-5 w-100" :class="(locating && no_cursor) ? notlocateCursor : ''"
      style="position: relative">
      <n-select size="large" class="region" :consistent-menu-width="false" v-model:show="show" filterable
        placeholder="請選擇欲新增裝置之區域" :options="options">
        <template v-if="show" #arrow>
          <md-search />
        </template>
      </n-select>
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
import MdSearch from '@vicons/ionicons4/MdSearch'
import { defineComponent, ref } from 'vue'
import MenuBar from '@/components/MenuBar.vue';
import AddDeviceInfo from '@/components/AddDeviceInfo.vue';

import locatePic from '../assets/pic/location.png'
import regionpic2 from '../assets/pic/regionpic2.jpg'

export default defineComponent({
  setup() {
    return {
      show: ref(false),
      options: [
        {
          label: 'A-1區',
          value: 'A-1'
        },
        {
          label: 'A-2區',
          value: 'A-2'
        },
        {
          label: 'A-3區',
          value: 'A-3'
        },
      ]
    }
  },
  components: {
    MdSearch,
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
      currentRegion: ''
    };
  },
  methods: {
    showData() {
      console.log(this.show)

    }
  }
});
</script>

<style scoped>
.region {
  width: 50vw;
  text-align: center;
}

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