<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column align-items-center p-5" style="width: 100%; position: relative;"
      :class="(locating && no_cursor) ? notlocateCursor : ''" @AddSuccess="AddSuccess()">

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
      <n-select v-if="$store.state.currvenue" @change="onChangeMethod($event)" size="large" class="region"
        :consistent-menu-width="true" v-model:show="show" v-model:value="areavalue" filterable placeholder="請選擇欲新增裝置之區域"
        :options="options">
        <template v-if="show" #arrow>
          <md-search />
        </template>
      </n-select>
      <button v-if="$store.state.currvenue" class="locateBtn my-2 " @click="clickBtn()" :style="clickBtnFlag()">
        <img :src="icon" @mouseover="icon = locatePic" @mouseleave="icon = locatePic_change">
      </button>

      <div v-if="$store.state.currvenue" id="Canvas" class="frame" :class="(locating) ? notlocateCursor : normalCursor"
        @click="add_device = true; no_cursor = false; ">
        <img v-if="areapic != ''" :src="'../../images/' + areapic + '.jpg'"
          :class="(locating && no_cursor) ? canlocateCursor : normalCursor" alt="尚未選取區域"
          @mousedown="getCursorValue($event)" ref="Canvas">
        <div v-for="item in currentdevice" :key="item">
          <img :src="already_locate" :style="styleobj" v-on="setPosition(item.x, item.y)">
        </div>
      </div>
      <div id="draggable">
        <AddDeviceInfo :info="propdata" style="cursor: default;" v-if="frame_status && add_device"
          @close="frame_status = false; add_device = false; locating = false; no_cursor = true; this.propdata = []; this.clickBtnStatus = false">
        </AddDeviceInfo>
      </div>

    </div>

  </div>
</template>

<script>
import $ from 'jquery'
import 'jquery-ui-dist/jquery-ui.js'
import 'jquery-ui-dist/jquery-ui.css'
import axios from 'axios'
import MdSearch from '@vicons/ionicons4/MdSearch'
import { defineComponent, ref, reactive } from 'vue'
import MenuBar from '@/components/MenuBar.vue';
import AddDeviceInfo from '@/components/AddDeviceInfo.vue';

import locatePic from '../assets/pic/location.png'
import locatePic_change from '../assets/pic/location_change.png'
import already_locate from '../assets/pic/already_locate.png'

export default defineComponent({
  setup() {
    let styleobj = reactive({
      width: '20px',
      height: '20px',
      position: 'absolute',
      top: '',
      left: ''
    });
    const setPosition = (x, y) => {
      styleobj.top = y + 'px'
      styleobj.left = x + 'px'
    }
    return {
      setPosition,
      styleobj,
      show: ref(false),
      options: [],
      propdata: [],
    }
  },
  components: {
    MdSearch,
    MenuBar,
    AddDeviceInfo,
  },
  data() {
    return {
      icon: locatePic_change,
      locatePic: locatePic,
      locatePic_change: locatePic_change,
      clickBtnStatus: false,
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
      frameBoundary: {
        'x': 0,
        'y': 0,
      },
      // areavalue: this.$store.state.regionAddName,
      areavalue: null,
      areapic: '',
      currentdevice: [],
    };
  },
  methods: {
    onChangeMethod(event) {
      this.currentdevice = []
      this.areavalue = event
      if (this.areavalue != null) {
        this.areapic = this.$store.state.currentvenue.toString() + "_" + this.areavalue.toString()
        this.fetchPicInfo()
      }
    },
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
    AddSuccess(areaname) {
      this.areavalue = areaname
      this.areapic = this.$store.state.currentvenue.toString() + "_" + this.areavalue.toString()
      console.log(this.areavalue)
      console.log('addcsda')
      console.log(this.areapic)
    },
    getCursorValue(event) {
      if (this.frame_status == true && this.locating == true) {
        let temp = this.$refs.Canvas

        this.frameBoundary.x = temp.getBoundingClientRect().x
        this.frameBoundary.y = temp.getBoundingClientRect().y

        this.mouse.x = event.clientX
        this.mouse.y = event.clientY
        // TODO: 應該要標記icon給目前要新增裝置之點

        this.propdata.push({
          'Xaxis': this.mouse.x - this.frameBoundary.x, 'Yaxis': this.mouse.y - this.frameBoundary.y, 'Area': this.areavalue, 'Venue': this.$store.state.currentvenue
        })
        // console.log(this.propdata)
      }
    },
    clickBtn() {
      if (this.clickBtnStatus) {
        this.frame_status = false;
        this.locating = false;
        this.clickBtnStatus = false
      }
      else {
        this.frame_status = true;
        this.locating = true;
        this.clickBtnStatus = true
      }
    },
    clickBtnFlag: function () {
      var style = {};
      if (this.clickBtnStatus) {
        style.backgroundColor = 'rgba(0, 0, 0, 0.2)';
      }
      else {
        style.backgroundColor = 'transparent';
      }
      return style;
    },
    async fetchPicInfo() {
      let devices
      await axios({
        method: 'get',
        baseURL: this.$store.state.api + '/deviceInfo',
        'Content-Type': 'application/json',
      })
        .then((response) => devices = response.data)
        .catch((err) => { console.error(err) })


      for (let i = 0; i < Object.values(devices).length; i++) {
        if (devices[i].Area === this.areavalue) {
          this.currentdevice.push({ 'x': devices[i].Xaxis, 'y': devices[i].Yaxis })
        }
      }
      // console.log(this.currentdevice)
    },
  },
  mounted() {
    this.fetchApi()
    if (this.$store.state.currvenue == false) {
      this.$router.push('/')
    }
    $('#draggable').draggable();
  }
});
</script>

<style scoped>
#draggable {
  position: absolute;
  top: 20vh;
  left: 25vw;
}

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


.frame {
  width: 550px;
  height: 550px;
  box-shadow: 0 0 5px 0 rgba(0, 0, 0, 10%);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
  position: relative;
}


.frame img {
  margin: 20px;
  width: 500px;
  height: 500px;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 55%);
  border-radius: 5px;
  font-weight: bold;
  font-size: 24px;
  color: rgba(0, 0, 0, 0.5);
}

.locateCursor {
  cursor: url('../assets/pic/locate_green2.png'), pointer;
}

.notlocateCursor {
  cursor: url('../assets/pic/no_locate.png'), pointer;
}

.normalCursor {
  cursor: default;
}
</style>