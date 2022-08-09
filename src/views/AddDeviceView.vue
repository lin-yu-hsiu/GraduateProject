<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column align-items-center p-5" style="width: 100%; position: relative;"
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
      <n-select v-if="$store.state.currvenue && freeBLEFlag" @change="onChangeMethod($event)" size="large"
        class="region" :consistent-menu-width="false" v-model:show="show" v-model:value="areavalue" filterable
        placeholder="請選擇欲新增裝置之區域" :options="options">
        <template v-if="show" #arrow>
          <md-search />
        </template>
      </n-select>
      <button v-if="$store.state.currvenue && freeBLEFlag" class="locateBtn mb-3"
        @click="frame_status = true; locating = true;" :style="clickBtnFlag()">
        <img :src="locatePic">
      </button>
      <div v-if="$store.state.currvenue && freeBLEFlag" class="frame" @click="add_device = true; no_cursor = false;"
        @mousedown="getCursorValue">
        <img :src="areapic" :class="(locating && no_cursor) ? canlocateCursor : normalCursor" alt="尚未選取區域">
      </div>
      <!-- <vue-drawing-canvas v-if="$store.state.currvenue && freeBLEFlag" ref="VueCanvasDrawing" v-model:image="image"
        :width="600" :height="400" :stroke-type="strokeType" :color="color" :background-image="backgroundImage"
        saveAs="png" :styles="{
        
        }" :lock="disabled" @mousemove="getCoordinate($event)" :additional-images="additionalImages" /> -->


      <div>
        <!-- class="moveable" -->
        <AddDeviceInfo class="moveable" :info="propdata" style="cursor: default;" v-if="frame_status && add_device"
          @close="frame_status = false; add_device = false; locating = false; no_cursor = true; this.propdata = []; this.BLEUUID = null; areavalue = null">
        </AddDeviceInfo>
      </div>

      <Moveable v-bind="moveable" @drag="handleDrag" />
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
// import VueDrawingCanvas from "vue-drawing-canvas";
import Moveable from "vue3-moveable";
import AddDeviceInfo from '@/components/AddDeviceInfo.vue';

import locatePic from '../assets/pic/location.png'
import pic from '../assets/region/regionpic1.jpg'
import already_locate from '../assets/pic/already_locate.png'

export default defineComponent({
  setup() {
    return {
      show: ref(false),

      options: [],
      propdata: [],
    }
  },
  components: {
    MdSearch,
    MenuBar,
    AddDeviceInfo,
    // VueDrawingCanvas,
    Moveable
  },
  data() {
    return {
      locatePic: locatePic,
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
      BLEUUID: null,
      areavalue: null,
      areapic: '',
      //---------------------------
      x: 0,
      y: 0,
      image: "",
      disabled: false,
      color: "#000000",
      strokeType: "dash",
      backgroundImage: pic,
      additionalImages: [],
      //---------------------------
      moveable: {
        target: [".moveable"],
        draggable: true,
        throttleDrag: 1,
        origin: false,
      },
    };
  },
  // watch: {
  //   areavalue() {
  //     this.onChangeMethod()
  //   }
  // },
  methods: {
    async onChangeMethod(event) {
      this.areavalue = event
      let areas
      await axios({
        method: 'get',
        baseURL: this.$store.state.api + '/table/Map',
        'Content-Type': 'application/json',
      })
        .then((response) => areas = response.data)
        .catch((err) => { console.error(err) })

      for (let i = 0; i < Object.values(areas).length; i++) {
        if (areas[i].Area === this.areavalue && areas[i].Venue === this.$store.state.currentvenue) {
          this.areapic = areas[i].Route
          break
        }
      }
      console.log(this.areapic)
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
      this.BLEUUID = index
    },
    clickBtnFlag: function () {
      var style = {};
      if (this.locating) {
        style.backgroundColor = 'rgba(0, 0, 0, 0.2)';
      }
      return style;
    },
    getCursorValue(event) {
      this.mouse.x = event.clientX
      this.mouse.y = event.clientY

      // TODO: 應該要標記icon給目前要新增裝置之點
      this.propdata.push({
        'UUID': this.BLEUUID, 'Xaxis': this.mouse.x, 'Yaxis': this.mouse.y, 'Area': this.areavalue, 'Venue': this.$store.state.currentvenue
      })
      console.log(this.propdata)
    },
    //-----------------------------------
    listItemStyle: function (index) {
      var style = {};
      if (index === this.BLEUUID) {
        style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        style.color = 'rgba(255, 255, 255, 1)';
      }
      return style;
    },
    handleDrag({ target, transform }) {
      console.log("onDrag", transform, target);
      target.style.transform = transform;
    },
    //-----------------------------
    async setImage(event) {
      let URL = window.URL;
      this.backgroundImage = URL.createObjectURL(event.target.files[0]);
      await this.$refs.VueCanvasDrawing.redraw();
    },
    async setWatermarkImage(event) {
      let URL = window.URL;
      this.watermark = {
        type: "Image",
        source: URL.createObjectURL(event.target.files[0]),
        x: 0,
        y: 0,
        imageStyle: {
          width: 600,
          height: 400,
        },
      };
      await this.$refs.VueCanvasDrawing.redraw();
    },
    getCoordinate(event) {
      let coordinates = this.$refs.VueCanvasDrawing.getCoordinates(event);
      this.x = coordinates.x;
      this.y = coordinates.y;
    },
    getStrokes() {
      window.localStorage.setItem(
        "vue-drawing-canvas",
        JSON.stringify(this.$refs.VueCanvasDrawing.getAllStrokes())
      );
      alert(
        "Strokes saved, reload your browser to see the canvas with previously saved image"
      );
    },
    removeSavedStrokes() {
      window.localStorage.removeItem("vue-drawing-canvas");
      alert("Strokes cleared from local storage");
    },
  },

  mounted() {
    this.fetchApi()
    this.fetchUUID()
    if ("vue-drawing-canvas" in window.localStorage) {
      this.initialImage = JSON.parse(
        window.localStorage.getItem("vue-drawing-canvas")
      );
    }
  }
});
</script>

<style scoped>
.moveable {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  white-space: nowrap;
  border: none;
  outline: none;
}

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

.frame {
  width: 100%;
  height: 100%;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 25%);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 5px;
}


.frame img {
  height: 100%;
  width: 100%;
  /* position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: 0 auto; */

  /* object-fit: fill; */

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