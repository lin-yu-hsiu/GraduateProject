<template>
  <div class="detailFrameInfo d-flex justify-content-evenly align-items-center mt-1 mx-3"
    :class="[isRemoving ? removeClass : '', isEditing ? editClass : '', deviceStatus ? '' : error]">
    <div class="d-flex justify-content-center" :class="[isRemoving ? removeHidden : '']" style="width: 100px">
      <button class="detailBtn p-0" v-if="!isEditing && !isRemoving" @click="isEditing = true"
        @mouseover="icon1 = edit_hover" @mouseleave="icon1 = edit">
        <img :src="icon1" style="width: 40px; height: 40px">
      </button>
      <button class="detailBtn p-0" v-if="!isEditing && !isRemoving" @click="isRemoving = true"
        @mouseover="icon2 = remove_hover" @mouseleave="icon2 = remove">
        <img :src="icon2" style="width: 30px; height: 35px">
      </button>
      <button name="CommitEdit" v-if="isEditing" class="detailBtn p-0 ms-1" @click="editChange"
        @mouseover="icon3 = yes_hover" @mouseleave="icon3 = yes">
        <img :src="icon3" style="width: 45px; height: 45px">
      </button>
      <button v-if="isEditing" class="detailBtn p-0" @click="isEditing = false" @mouseover="icon4 = no_hover"
        @mouseleave="icon4 = no">
        <img :src="icon4" style="width: 45px; height: 45px">
      </button>
    </div>
    <div v-if="isRemoving">
      <div class="d-flex justify-content-around align-items-center">
        <button v-if="isRemoving" class="detailBtn p-0" @click="removeChange" @mouseover="icon3 = yes_hover"
          @mouseleave="icon3 = yes">
          <img :src="icon3" style="width: 50px; height: 50px">
        </button>
        <button v-if="isRemoving" class="detailBtn p-0" @click="isRemoving = false" @mouseover="icon4 = no_hover"
          @mouseleave="icon4 = no">
          <img :src="icon4" style="width: 50px; height: 50px">
        </button>
      </div>
      <div v-if="isRemoving">確定刪除此裝置 ?</div>
    </div>

    <div class="text-center" :class="[isRemoving ? removeHidden : '']" style="width: 100px; color: #000000;">
      {{ deviceInfo.Place }}</div>

    <div class="d-flex justify-content-center" :class="[isRemoving ? removeHidden : '']" style="width: 100px">
      <img v-if="deviceInfo.Battery"
        :src="require('../assets/pic/' + 'battery' + (deviceInfo.Battery.substr(0, deviceInfo.Battery.length - 1)).toString() + '.png')"
        :class="[isRemoving ? removeHidden : '']" style="width: 60px;">
    </div>

    <textarea v-if="isEditing" name="" id="messageContentEditing" class="scroll edit scroll_white"
      :class="[isRemoving ? removeHidden : '']" cols="10" rows="2" style="width: 150px"
      v-model="deviceInfo.Message"></textarea>
    <textarea v-else name="" disabled id="messageContent" class="scroll" :class="[isRemoving ? removeHidden : '']"
      cols="10" rows="2" style="width: 150px" v-model="deviceInfo.Message"></textarea>


    <n-switch size="large" v-if="isEditing" v-model:value="deviceInfo.Status" :class="[isRemoving ? removeHidden : '']"
      style="width: 100px;">
    </n-switch>
    <n-switch size="large" v-else disabled v-model:value="deviceInfo.Status" :class="[isRemoving ? removeHidden : '']"
      style="width: 100px;">
    </n-switch>


    <textarea v-if="isEditing" name="" id="psEditing" class="scroll edit scroll_white"
      :class="[isRemoving ? removeHidden : '']" cols="10" rows="2" style="width: 150px"
      v-model="deviceInfo.Note"></textarea>
    <textarea v-else name="" disabled id="psContent" class="scroll" :class="[isRemoving ? removeHidden : '']" cols="10"
      rows="2" style="width: 150px" v-model="deviceInfo.Note"></textarea>
  </div>
</template>

<script>
import axios from 'axios'
import { defineComponent } from "vue";

import edit from '../assets/pic/edit_green.png'
import edit_hover from '../assets/pic/edit_green_hover.png'
import remove from '../assets/pic/trash.png'
import remove_hover from '../assets/pic/trash_hover.png'
import yes from '../assets/pic/yes.png'
import yes_hover from '../assets/pic/yes_hover.png'
import no from '../assets/pic/no.png'
import no_hover from '../assets/pic/no_hover.png'
import battery100 from '../assets/pic/battery100.png'
import battery50 from '../assets/pic/battery50.png'
import battery0 from '../assets/pic/battery0.png'


export default defineComponent({
  props: {
    device: {
      type: Object,
    }
  },
  watch: {
    device(newVal) {
      this.deviceInfo = newVal
    }
  },
  data() {
    return {
      // 以下為props ----------------------------------
      deviceInfo: this.device,
      // 以下為variables ------------------------------
      isEditing: false,
      editClass: 'editClass',
      isRemoving: false,
      removeClass: 'removeClass',
      removeHidden: 'removehidden',
      deviceStatus: false,
      error: 'error',
      // 以下為icons ----------------------------------
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
      battery50: battery50,
      battery0: battery0,
    }
  },
  methods: {
    async editChange() {
      const body = {
        'UUID': this.deviceInfo.UUID,
        'Status': this.deviceInfo.Status,
        'Message': this.deviceInfo.Message,
        'Note': this.deviceInfo.Note,
      }
      const json = JSON.stringify(body);
      const res = await axios.post(this.$store.state.api + '/modifyBLE', json, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      console.log(res);
      this.isEditing = false
    },
    async removeChange() {
      const body = {
        'UUID': this.deviceInfo.UUID,
      }
      const json = JSON.stringify(body);
      const res = await axios.post(this.$store.state.api + '/deleteBLE', json, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      console.log(res);
      this.isRemoving = false
      this.$emit('remove')
    },
  },
  mounted() {
  }
})
</script>

<style scoped>
.detailFrameInfo {
  font-weight: bold;
  font-size: 18px;
  padding: 8px 0px;
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

#psContent {
  outline: none;
  border: solid .5px rgba(0, 0, 0, 15%);
  padding: 4px 8px;
  font-size: 16px;
  border-radius: 5px;
  resize: none;
}

.error {
  background-color: rgba(255, 0, 0, 15%);
  border-radius: 5px;
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
  border: solid 0.5px rgba(0, 0, 0, 10%);
}

.removeClass {
  background-color: rgba(0, 0, 0, 100%);
  color: #ffffff;
  border-radius: 10px;
  padding: 0;
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