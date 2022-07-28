<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column align-items-center w-100 p-5" style="width: 100%"
      :class="(locating && no_cursor) ? notlocateCursor : ''">
      <div class="d-flex justify-content-center align-items-center">
        <div style="font-weight: bold; font-size: 24px;color: rgba(0, 0, 0, 50%);">您目前所在場館為 </div>
        <div style="font-weight: 800; font-size: 26px; color: rgba(0, 0, 0, 90%); margin-left: 10px;">
          {{
              $store.state.currentvenue
          }}
        </div>
      </div>
      <n-select v-if="$store.state.currvenue" size="large" class="region" :consistent-menu-width="false"
        v-model:show="show" filterable placeholder="請選擇欲新增裝置之區域" :options="options">
        <template v-if="show" #arrow>
          <md-search />
        </template>
      </n-select>
      <button v-if="$store.state.currvenue" class="locateBtn mb-3" @click="frame_status = true; locating = true;">
        <img :src="locatePic">
      </button>
      <div v-if="$store.state.currvenue" class="frame" :class="(locating && no_cursor) ? canlocateCursor : normalCursor"
        @click="add_device = true; no_cursor = false;" @mousedown="getCursorValue">
        <img :src="pic">
      </div>
      <AddDeviceInfo style="cursor: default;" v-if="frame_status && add_device"
        @close="frame_status = false; add_device = false; locating = false; no_cursor = true"></AddDeviceInfo>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MdSearch from '@vicons/ionicons4/MdSearch'
import { defineComponent, ref } from 'vue'
import MenuBar from '@/components/MenuBar.vue';
import AddDeviceInfo from '@/components/AddDeviceInfo.vue';

import locatePic from '../assets/pic/location.png'
import pic from '../assets/region/regionpic1.jpg'

export default defineComponent({
  setup() {
    return {
      show: ref(false),
      options: [],
      mouse: {
        'x': 0,
        'y': 0,
      }
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
      pic: pic,
      frame_status: false,
      add_device: false,
      locating: false,
      canlocateCursor: 'locateCursor',
      notlocateCursor: 'notlocateCursor',
      normalCursor: 'normalCursor',
      no_cursor: true,
    };
  },
  methods: {
    async fetchApi() {
      let regions = []
      await axios({
        method: 'get',
        baseURL: this.$store.state.api + '/deviceInfo',
        'Content-Type': 'application/json',
      })
        .then((response) => regions = response.data)
        .catch((err) => { console.error(err) })
      let regionSet = new Set()
      for (let i = 0; i < regions.length; i++) {
        if (regions[i].Venue == this.$store.state.currentvenue) {
          regionSet.add(regions[i].Area)
        }
      }
      regionSet.forEach((item) => this.options.push({ 'label': item, 'value': item }));
    },
    getCursorValue(event) {
      this.mouse.x = event.clientX
      this.mouse.y = event.clientY
      console.log(this.mouse)
    }
  },
  mounted() {
    this.fetchApi()
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
  background-color: rgba(0, 0, 0, 10%);
}

.frame {
  width: 80vw;
  height: 100%;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 25%);
  position: relative;
}


.frame img {
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: 0 auto;
  border-radius: 5px;
  /* padding: 20px 0;*/
  position: absolute;
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