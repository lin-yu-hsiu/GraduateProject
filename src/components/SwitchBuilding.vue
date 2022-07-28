<template>
  <div class="regionList">
    <div style="font-weight: bold; font-size: 26px;">{{ regionInfo }}
    </div>
    <button class="detailBtn p-0" @click="isRemoving = true" @mouseover="icon = remove_hover"
      @mouseleave="icon = remove">
      <img :src="icon" style="width: 36px; height: 42px">
    </button>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import regionpic1 from '../assets/region/regionpic1.jpg'
import regionpic2 from '../assets/region/regionpic2.jpg'
import remove from '../assets/pic/trash.png'
import remove_hover from '../assets/pic/trash_hover.png'

export default defineComponent({
  props: {
    region: {
      required: true
    }
  },
  data() {
    return {
      regionInfo: this.region,
      icon: remove,
      remove: remove,
      remove_hover: remove_hover,
      regionpic1: regionpic1,
      regionpic2: regionpic2,
    }
  },
  methods: {

  },
  mounted() {

  },
});
</script>

<style scoped>
.regionList {
  width: 320px;
  height: 200px;
  background: linear-gradient(to bottom, #ffffff 0%, rgba(142, 142, 142, 50%) 100%);
  box-shadow: 0 10px 10px 0 rgba(0, 0, 0, 25%);
  display: flex;
  align-items: center;
  justify-content: space-between;
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

.detailBtn {
  background-color: transparent;
  border: none;
}
</style>