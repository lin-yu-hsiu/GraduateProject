<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column p-5 w-100 mx-auto">
      <div class="d-flex justify-content-center align-items-center">
        <div style="font-weight: bold; font-size: 24px;color: rgba(0, 0, 0, 50%);">您目前所在場館為 </div>
        <div style="font-weight: 800; font-size: 26px; color: rgba(0, 0, 0, 90%); margin-left: 10px;">
          {{
              $store.state.currentvenue
          }}
        </div>
      </div>
      <div v-if="$store.state.currvenue" class="d-flex justify-content-center align-items-center my-5">
        <div class="title mx-3">
          區域名稱
        </div>
        <input id="RegionName" class="regionName" type="text" placeholder="欲新增之名稱">
      </div>
      <div v-if="$store.state.currvenue" class="picRegion d-flex justify-content-center align-items-center">
        <n-upload id="RegionPic" list-type="image" class="d-flex flex-column align-items-center" action="https://">
          <button class="clickToLoad">
            <img :src="loadpic" style="width: 45px; height: 45px">
            點擊以匯入平面圖 ...
          </button>
        </n-upload>
      </div>
      <button v-if="$store.state.currvenue" class="clickToStore" @click="validate">
        <img :src="store_black" style="width: 45px; height: 55px">
      </button>
    </div>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue';
import loadpic from '../assets/pic/loadpic.png'
import store_black from '../assets/pic/store_black.png'

export default {
  components: {
    MenuBar
  },
  data() {
    return {
      store_black: store_black,
      loadpic: loadpic,
      currentBuilding: 'A 棟'
    };
  },
  methods: {
    validate() {

    }
  }
};
</script>

<style scoped>
.picRegion {
  width: 70vw;
  height: 100%;
  max-width: 1500px;
  background-color: #D9D9D9;
  box-shadow: 0 0 30px 0 rgba(0, 0, 0, 25%) inset;
  margin: 0 auto;
}

.title {
  font-size: 24px;
  font-weight: 800;
  border-radius: 20px;
  text-align: center;
  background-color: #ffffff;
  width: 150px;
  height: 45px;
  line-height: 2;
}

.regionName {
  border-radius: 20px;
  font-size: 18px;
  text-align: center;
  font-weight: 500;
  background-color: #ffffff;
  outline: none;
  border: none;
  width: 200px;
  height: 40px;
}

.clickToLoad {
  border: none;
  font-size: 18px;
  font-weight: bold;
  border-radius: 5px;
  padding: 8px;
  outline: none;
  background: linear-gradient(to right, #ffffff 0%, #D9D9D9 100%);
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 15%);
}

.clickToLoad:hover {
  background-color: #D9D9D9;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 10%) inset;
  color: #2b2b2b;
}

.clickToStore {
  background-color: transparent;
  border: none;
  margin: 30px auto;
  padding: 4px 8px;
  transition: all 100ms ease;
  border-radius: 15px;
}

.clickToStore:hover {
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 15%) inset,
    0 -2px 4px 0 rgba(0, 0, 0, 15%) inset;
}
</style>