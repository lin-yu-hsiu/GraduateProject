<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column align-items-center p-5" style="width: 100%"
      :class="(locating && no_cursor) ? notlocateCursor : ''">
      <div style="font-weight: bold; font-size: 18px;color: rgba(0, 0, 0, 30%); align-self: flex-start;">
        /
        {{
            $store.state.currentvenue
        }}
        / 新增裝置
      </div>
      <div class="d-flex justify-content-center align-items-center">
        <div style="font-weight: bold; font-size: 24px;color: rgba(0, 0, 0, 50%);">您目前所在場館為 </div>
        <div style="font-weight: 800; font-size: 26px; color: rgba(0, 0, 0, 90%); margin-left: 10px;">
          {{
              $store.state.currentvenue
          }}
        </div>
      </div>
      <n-select v-if="$store.state.currvenue && freeBLEFlag" size="large" class="region" :consistent-menu-width="false"
        v-model:show="show" v-model:value="areavalue" filterable placeholder="請選擇欲新增裝置之區域" :options="options">
        <template v-if="show" #arrow>
          <md-search />
        </template>
      </n-select>
      <button v-if="$store.state.currvenue && freeBLEFlag" class="locateBtn mb-3"
        @click="frame_status = true; locating = true;">
        <img :src="locatePic">
      </button>
      <div v-if="$store.state.currvenue && freeBLEFlag" class="frame"
        :class="(locating && no_cursor) ? canlocateCursor : normalCursor" @click="add_device = true; no_cursor = false;"
        @mousedown="getCursorValue">
        <img :src="pic">
      </div>
      <AddDeviceInfo :info="propdata" style="cursor: default;" v-if="frame_status && add_device"
        @close="frame_status = false; add_device = false; locating = false; no_cursor = true"></AddDeviceInfo>
    </div>
    <div class="listFreeBLE" v-if="this.$store.state.currvenue">
      <div style="font-weight: bold; font-size: 18px; text-align: center; word-wrap: none; margin-bottom: 50px;">
        選取進行配對之裝置</div>
      <div style="height: 55vh">
        <div v-if="freeBLEFlag">
          <div :style="listItemStyle(ble)" v-for="ble in freeBLE" :key="ble.id" class="ble" @click="chooseBLE(ble)">
            {{ ble }}
          </div>
        </div>
        <div v-else style="font-weight: bold; font-size: 16px; text-align: center;color: rgba(0, 0, 0, 0.5)">目前無裝置可配對
        </div>
      </div>
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
import already_locate from '../assets/pic/already_locate.png'

export default defineComponent({
  setup() {
    return {
      show: ref(false),
      areavalue: ref(null),
      options: [],
      propdata: [],
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
      blechosen: 'blechosen',
      already_locate: already_locate,
      no_cursor: true,
      mouse: {
        'x': 0,
        'y': 0,
      },
      freeBLE: [],
      freeBLEFlag: false,
      chooseFlag: null,
    };
  },
  methods: {
    async fetchApi() {
      let regions
      await axios({
        method: 'get',
        baseURL: this.$store.state.api + '/table/',
        url: this.$store.state.currentvenue.toString(),
        'Content-Type': 'application/json',
      })
        .then((response) => regions = response.data)
        .catch((err) => { console.error(err) })

      let regionSet = new Set()
      for (let i = 0; i < Object.values(regions).length; i++) {
        if (regions[i].Venue == this.$store.state.currentvenue) {
          regionSet.add(regions[i].Area)
        }
      }
      regionSet.forEach((item) => this.options.push({ 'label': item, 'value': item }));
    },
    async fetchUUID() {
      let UUIDs
      await axios({
        method: 'get',
        baseURL: this.$store.state.api + '/newDevice',
        'Content-Type': 'application/json',
      })
        .then((response) => UUIDs = response.data)
        .catch((err) => { console.error(err) })

      if (UUIDs['free'].length != 0) {
        this.freeBLEFlag = true
        for (let i = 0; i < UUIDs['free'].length; i++) {
          this.freeBLE.push(UUIDs['free'][i])
        }
      }
      else {
        return
      }
    },
    chooseBLE(index) {
      this.chooseFlag = index
    },
    listItemStyle: function (index) {
      var style = {};
      if (index === this.chooseFlag) {
        style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        style.color = 'rgba(255, 255, 255, 1)';
      }
      return style;
    },
    getCursorValue(event) {
      this.mouse.x = event.clientX
      this.mouse.y = event.clientY

      // TODO: 應該要記錄目前要新增裝置之點
      this.propdata.push({
        'UUID': this.chooseFlag, 'Xaxis': this.mouse.x, 'Yaxis': this.mouse.y, 'Area': this.areavalue, 'Venue': this.$store.state.currentvenue
      })
      console.log(this.propdata)
    },

  },
  mounted() {
    this.fetchApi()
    this.fetchUUID()
  }
});
</script>

<style scoped>
.region {
  width: 50vw;
  text-align: center;
}

.listFreeBLE {
  min-width: 250px;
  width: 250px;
  background-color: rgba(240, 248, 255, 0.2);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.ble {
  background-color: rgba(240, 248, 255, 0.8);
  height: 50px;
  text-align: center;
  font-size: 22px;
  font-weight: bold;
  line-height: 2.2;
  border-radius: 10px;
  margin: 10px 20px;
}

.ble:hover {
  color: rgba(0, 0, 0, 0.8);
  background-color: rgba(217, 217, 217, 0.7);
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
  background-color: rgba(0, 0, 0, 20%);
}

.frame {
  width: 100%;
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
  position: absolute;
  padding: 20px 15px;
  object-fit: contain;
}

.locateCursor {
  cursor: url('../assets/pic/locate_green.png'), pointer;
}

.notlocateCursor {
  cursor: url('../assets/pic/no_locate.png'), pointer;
}

.normalCursor {
  cursor: default;
}
</style>