<template>
  <div class="regionList">
    <div style="font-weight: bold; align-self: start; font-size: 26px;">{{ regionname }}</div>
    <button class="forDetail">
      <img :src="fordetail">
      查看細節
    </button>
  </div>
  <!-- <DeviceRegion style="position: absolute; top:20vh; left:25vw"></DeviceRegion> -->
</template>

<script>
// import DeviceRegion from './DeviceRegion.vue'
import detail from '../assets/pic/fordetail.png'
import good from '../assets/pic/good.png'

export default {
  components: {
    // DeviceRegion
  },
  data() {
    return {
      regionname: "A棟",
      message: '',
      fordetail: detail,
      devicegood: good
    }
  },
}
</script>
    <style scoped>
    .regionList {
      width: 400px;
      height: 250px;
      background: linear-gradient(to bottom, #ffffff 0%, rgba(142, 142, 142, 50%) 100%);
      box-shadow: 0 10px 10px 0 rgba(0, 0, 0, 25%);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-around;
      border-radius: 0 0 20px 20px;
      padding: 20px;
    }
    
    .regionList:hover {
      box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 5%) inset;
    }
    
    .forDetail {
      background-color: #464646;
      color: #ffffff;
      font-weight: bold;
      font-size: 24px;
      width: 220px;
      height: 60px;
      border-radius: 10px;
      padding: 4px 8px;
      border: none;
    }
    
    .forDetail:hover {
      background-color: #2c2c2c;
    }
    
    .no_mistake {
      border: ridge 3px #0FA958;
    }
    
    .mistake {
      border: ridge 3px #df4a4a;
    }
    </style>
