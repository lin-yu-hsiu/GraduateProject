<template>
  <div class="detailFrameInfo d-flex justify-content-evenly align-items-center mt-3 mx-3"
    :class="[isRemoving ? removeClass : '', isEditing ? editClass : '']">
    <div class="d-flex justify-content-center" :class="[isRemoving ? removeHidden : '']" style="width: 100px">
      <button class="detailBtn p-0" v-if="!isEditing && !isRemoving" @click="isEditing = true"
        @mouseover="icon1 = edit_hover" @mouseleave="icon1 = edit">
        <img :src="icon1" style="width: 40px; height: 40px">
      </button>
      <button class="detailBtn p-0" v-if="!isEditing && !isRemoving" @click="isRemoving = true"
        @mouseover="icon2 = remove_hover" @mouseleave="icon2 = remove">
        <img :src="icon2" style="width: 30px; height: 35px">
      </button>
      <button v-if="isEditing" class="detailBtn p-0 ms-1" @mouseover="icon3 = yes_hover" @mouseleave="icon3 = yes">
        <img :src="icon3" style="width: 45px; height: 45px">
      </button>
      <button v-if="isEditing" class="detailBtn p-0" @click="isEditing = false" @mouseover="icon4 = no_hover"
        @mouseleave="icon4 = no">
        <img :src="icon4" style="width: 45px; height: 45px">
      </button>
    </div>
    <div v-if="isRemoving">
      <div class="d-flex justify-content-around align-items-center">
        <button v-if="isRemoving" class="detailBtn p-0" @mouseover="icon3 = yes_hover" @mouseleave="icon3 = yes">
          <img :src="icon3" style="width: 50px; height: 50px">
        </button>
        <button v-if="isRemoving" class="detailBtn p-0" @click="isRemoving = false" @mouseover="icon4 = no_hover"
          @mouseleave="icon4 = no">
          <img :src="icon4" style="width: 50px; height: 50px">
        </button>
      </div>
      <div v-if="isRemoving">確定刪除此裝置 ?</div>
    </div>
    <input v-if="isEditing" class="text-center edit scroll_white" :class="[isRemoving ? removeHidden : '']"
      style="width: 100px;" type="text" placeholder="大門口">
    <div v-else class="text-center" :class="[isRemoving ? removeHidden : '']" style="width: 100px;">大門口</div>
    <div class="d-flex justify-content-center" :class="[isRemoving ? removeHidden : '']" style="width: 100px">
      <img :src="battery90" :class="[isRemoving ? removeHidden : '']" style="width: 60px; height: 30px">
    </div>
    <textarea v-if="isEditing" name="" id="messageContentEditing" class="scroll edit scroll_white"
      :class="[isRemoving ? removeHidden : '']" cols="10" rows="2" style="width: 150px"></textarea>
    <textarea v-else name="" id="messageContent" class="scroll" :class="[isRemoving ? removeHidden : '']" cols="10"
      rows="2" style="width: 150px"></textarea>
    <n-switch :class="[isRemoving ? removeHidden : '']" style="width: 100px;"></n-switch>
  </div>
</template>

<script>
import edit from '../assets/pic/edit_green.png'
import edit_hover from '../assets/pic/edit_green_hover.png'
import remove from '../assets/pic/trash.png'
import remove_hover from '../assets/pic/trash_hover.png'
import yes from '../assets/pic/yes.png'
import yes_hover from '../assets/pic/yes_hover.png'
import no from '../assets/pic/no.png'
import no_hover from '../assets/pic/no_hover.png'
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
      icon3: yes,
      icon4: no,
      edit: edit,
      edit_hover: edit_hover,
      remove: remove,
      remove_hover: remove_hover,
      yes: yes,
      yes_hover: yes_hover,
      no: no,
      no_hover: no_hover,
      battery100: battery100,
      battery90: battery90,
      battery80: battery80,
      battery60: battery60,
      battery50: battery50,
      battery30: battery30,
      battery20: battery20,
      isEditing: false,
      editClass: 'editClass',
      isRemoving: false,
      removeClass: 'removeClass',
      removeHidden: 'removehidden',
    }
  },
  methods: {

  }
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
  border: solid .5px rgba(0, 0, 0, 15%);
  padding: 4px 8px;
  font-size: 16px;
  border-radius: 5px;
  resize: none;
}

.edit {
  outline: none;
  border: solid .5px rgba(0, 0, 0, 5%);
  padding: 4px 8px;
  font-size: 16px;
  border-radius: 5px;
  background-color: rgba(0, 0, 0, 100%);
  resize: none;
  color: #ffffff;
}

.editClass {
  background-color: rgba(0, 0, 0, 5%);
  color: #ffffff;
  border-radius: 10px;
  padding: 8px 0px;
  box-shadow: 0 .5px 4px 0 rgba(0, 0, 0, 15%), 0 -.5px 4px 0 rgba(0, 0, 0, 15%);
}

.removeClass {
  background-color: rgba(0, 0, 0, 100%);
  color: #ffffff;
  border-radius: 10px;
  padding: 8px 0px;
  box-shadow: 0 .5px 4px 0 rgba(0, 0, 0, 75%), 0 -.5px 4px 0 rgba(0, 0, 0, 75%);
}

.removehidden {
  display: none;
}

.scroll {
  overflow-y: scroll;
  cursor: default;
}

.scroll::-webkit-scrollbar {
  width: 5px;
}

.scroll::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.25);
  border-radius: 5px;
}

.scroll::-webkit-scrollbar-thumb:hover {
  background-color: rgba(0, 0, 0, 0.4);
}

.scroll_white {
  overflow-y: scroll;
  cursor: default;
}

.scroll_white::-webkit-scrollbar {
  width: 5px;
}

.scroll_white::-webkit-scrollbar-thumb {
  background-color: rgba(255, 255, 255, 70%);
  border-radius: 5px;
}

.scroll_white::-webkit-scrollbar-thumb:hover {
  background-color: rgba(255, 255, 255, 30%);
}
</style>