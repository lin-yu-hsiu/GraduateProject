<template>
  <div class="regionList">
    <div style="font-weight: bold; align-self: start; font-size: 26px;">{{ regionInfo.name }}</div>
    <img :src="require('../assets/pic/' + regionInfo.thumbnail + '.jpg')" class="thumbNail">
  </div>
</template>

<script>
import regionpic1 from '../assets/pic/regionpic1.jpg'
import regionpic2 from '../assets/pic/regionpic2.jpg'

export default {
  props: {
    region: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      regionInfo: this.region,
      regionpic1: regionpic1,
      regionpic2: regionpic2,
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

.thumbNail {
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 25%);
  width: 300px;
  height: 150px;
  border-radius: 20px;
}
</style>