<template>
  <div class="detailFrameInfo d-flex justify-content-evenly align-items-center mt-3">
    <div class="d-flex justify-content-center" style="width: 100px">
      <button class="detailBtn p-0" @mouseover="icon1 = edit_hover" @mouseleave="icon1 = edit">
        <img :src="icon1" style="width: 40px; height: 40px">
      </button>
      <button class="detailBtn p-0" @mouseover="icon2 = remove_hover" @mouseleave="icon2 = remove">
        <img :src="icon2" style="width: 30px; height: 35px">
      </button>
    </div>
    <div class="text-center" style="width: 100px;">大門口</div>
    <div class="d-flex justify-content-center" style="width: 100px">
      <img :src="battery90" style="width: 60px; height: 30px">
    </div>
    <textarea name="" id="messageContent" cols="10" rows="2" style="width: 150px"></textarea>
    <n-switch style="width: 100px"></n-switch>
  </div>
</template>

<script>
import edit from '../assets/pic/edit_green.png'
import edit_hover from '../assets/pic/edit_green_hover.png'
import remove from '../assets/pic/trash.png'
import remove_hover from '../assets/pic/trash_hover.png'
import battery100 from '../assets/pic/battery100.png'
import battery90 from '../assets/pic/battery90.png'
import battery80 from '../assets/pic/battery80.png'
import battery60 from '../assets/pic/battery60.png'
import battery50 from '../assets/pic/battery50.png'
import battery30 from '../assets/pic/battery30.png'
import battery20 from '../assets/pic/battery20.png'

export default {
  data() {
    return {
      icon1: edit,
      icon2: remove,
      edit: edit,
      edit_hover: edit_hover,
      remove: remove,
      remove_hover: remove_hover,
      battery100: battery100,
      battery90: battery90,
      battery80: battery80,
      battery60: battery60,
      battery50: battery50,
      battery30: battery30,
      battery20: battery20,
    }
  },
}
</script>

<style scoped>
.detailFrameInfo {
  font-weight: bold;
  font-size: 18px;
}

.detailBtn {
  background-color: transparent;
  border: none;
}

#messageContent {
  outline: none;
  border: solid .5px rgba(0, 0, 0, 25%);
  padding: 4px 8px;
  border-radius: 5px;
}
</style>