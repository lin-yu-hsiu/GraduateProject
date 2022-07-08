<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column p-5 w-100">
      <div class="d-flex justify-content-center align-items-center my-5">
        <div class="title mx-3">
          區域名稱
        </div>
        <input class="regionName" type="text" placeholder="欲新增之名稱">
      </div>
      <div class="picRegion d-flex justify-content-center align-items-center">
        <button class="clickToLoad">
          <img :src="loadpic" style="width: 45px; height: 45px">
          點擊以匯入平面圖 ...
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue';
export default {
  components: {
    MenuBar
  },
  data() {
    return {
      loadpic: 'icon/loadpic.png'
    };
  },
};
</script>

<style scoped>
.picRegion {
  width: 70vw;
  height: 60vh;
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
  background: linear-gradient(to right, #ffffff 0%, #D9D9D9 100%);
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 15%);
}

.clickToLoad:hover {
  background-color: #D9D9D9;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 10%) inset;
  color: #2b2b2b;
}
</style>