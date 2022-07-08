<template>
  <div class="regionList">
    <div style="font-weight: bold; align-self: start; font-size: 26px;">{{ regionname }}</div>
    <img :src="thumbnail" class="thumbNail">
  </div>
</template>

<script>
import testpic1 from '../assets/pic/1.jpg'
// import testpic2 from '../assets/pic/2.jpg'
export default {
  data() {
    return {
      regionname: "A棟",
      thumbnail: testpic1
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