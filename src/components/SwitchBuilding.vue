<template>
  <div class="regionList" @click="switchVenue">
    <div style=" font-weight: bold; font-size: 26px;">{{ venueInfo.name }} 館</div>
    <button class="detailBtn p-0" v-if="this.$store.state.venueEditMode" @click="showModal = true"
      @mouseover="icon = remove_hover" @mouseleave="icon = remove">
      <img :src="icon" style="width: 30; height: 35px; z-index: 10;">
    </button>
    <n-modal v-model:show="showModal" type="warning" preset="dialog" title="確定刪除 ?"
      :content="'確認刪除 ' + venueInfo.name + ' 此場館'" positive-text="確定" negative-text="取消" @positive-click="removeVenue"
      style="font-weight: bold;" />
  </div>
</template>

<script>
import axios from 'axios'
import { defineComponent, inject, ref } from "vue";
import { useMessage } from 'naive-ui'
import remove from '../assets/pic/trash.png'
import remove_hover from '../assets/pic/trash_hover.png'

export default defineComponent({
  setup() {
    const reload = inject('reload')
    const message = useMessage()
    const update = () => {
      message.success('新增成功'),
        { duration: 1000 }
      reload()
    }
    const success = () => {
      message.success('切換成功')
    }
    const mistake = () => {
      message.error('無法切換場館，請先關閉編輯模式')
    }
    return {
      update,
      mistake,
      success,
      showModal: ref(false),
    }
  },
  props: {
    venue: {
      required: true
    }
  },
  data() {
    return {
      icon: remove,
      remove: remove,
      remove_hover: remove_hover,
      venueInfo: this.venue,
      removeflag: false,
      switchflag: true  //解決remove & switch同時發生
    }
  },
  methods: {
    switchVenue() {
      if (this.$store.state.venueEditMode == false) {
        this.$store.commit('switchRegion', this.venueInfo.name);
        this.success()
      }
      else {
        if (this.switchflag != true) {
          this.mistake()
        }
      }
    },
    async removeVenue() {
      const body = {
        'Venue': this.venueInfo.name,
      }
      const json = JSON.stringify(body);

      await axios({
        method: 'post',
        baseURL: this.$store.state.api + '/deleteVenue',
        headers: { 'Content-Type': 'application/json' },
        data: json
      })
        .then((response) => response = response.data)
        .catch((error) => console.log(error))

      this.removeflag = true
      this.$emit('removeDisplay', this.venueInfo.name, this.removeflag) //刪除此場館並回傳到父元件以更新畫面
      if (this.$store.state.currentvenue == this.venueInfo.name) {
        this.$store.state.currentvenue = '(需先切換場館)'
        this.$store.state.currvenue = false
      }
    },
    te() {

    }
  },
  mounted() {

  },
});
</script>

<style scoped>
.regionList {
  width: 300px;
  height: 180px;
  background: linear-gradient(to bottom, #ffffff 0%, rgba(142, 142, 142, 50%) 100%);
  box-shadow: 0 10px 10px 0 rgba(0, 0, 0, 25%);
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-radius: 20px;
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
  z-index: 11;
}
</style>