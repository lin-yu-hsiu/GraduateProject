<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column align-items-center p-5 w-100"
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
      <button v-if="$store.state.currvenue" class="locateBtn mb-3" @click="add_status = true; locating = true;">
        <img :src="locatePic">
      </button>
      <div v-if="$store.state.currvenue" class="frame">
        <img :src="pic" :class="locating ? canlocateCursor : ''" @click="add_device = true; no_cursor = false">
      </div>
      <AddDeviceInfo style="cursor: default;" v-if="add_status && add_device"
        @close="add_status = false; add_device = false; locating = false"></AddDeviceInfo>
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

export default defineComponent({
  setup() {
    return {
      show: ref(false),
      options: [],
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
      pic: '',
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
  background-color: rgba(0, 0, 0, 75%);
}

.frame {
  width: 80vw;
  height: 100%;
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