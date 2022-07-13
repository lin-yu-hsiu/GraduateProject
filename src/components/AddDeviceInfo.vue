<template>
  <div class="checkDevice p-5">
    <h3 class="text-center mb-5" style="font-weight: bold">欲新增裝置之必填資料</h3>
    <div class="d-flex justify-content-between mx-auto" style="width: 300px">
      <div class="subTitle">裝置編號</div>
      <div class="subTitle" disabled>1</div>
    </div>
    <div class="d-flex flex-column mx-auto align-items-center" style="width: 300px;height: 200px">
      <div class="subTitle my-4" style="align-self: flex-start">訊息內容</div>

      <textarea class="message scroll p-3"></textarea>
    </div>

    <button class="addBtn">
      <img id='addBtn' :src="store_black" style="width: 45px; height: 55px">
    </button>
    <div class="d-flex justify-content-center align-items-center mt-3" style="font-weight: 800;">
      <Icon icon="eos-icons:loading" color="rgba(0, 0, 0, 70%)" height="40" />
      <img :src="ok" class="me-3" style="width:30px; height:30px">
      確認此裝置已連上網
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { Icon } from '@iconify/vue';
import ok from '../assets/pic/ok.png'
import store_black from '../assets/pic/store_black.png'
import store_white from '../assets/pic/store_white.png'

export default defineComponent({
  components: {
    Icon,
  },
  data() {
    return {
      ok: ok,
      store_black: store_black,
      store_white: store_white
    }
  },
})
</script>

<style scoped>
.checkDevice {
  width: 500px;
  height: 500px;
  position: absolute;
  top: 20vh;
  left: auto;
  background-color: #ffffff;
  border-radius: 30px;
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 25%),
    0 -4px 20px 0 rgba(0, 0, 0, 25%);
}

.subTitle {
  width: 100px;
  height: 30px;
  background-color: rgba(201, 201, 201, 80%);
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 25%);
  font-weight: bold;
  text-align: center;
  line-height: 2;
}

.message {
  background-color: rgba(217, 217, 217, 50%);
  width: 350px;
  height: 100px;
  border: none;
  outline: none;
  padding: 8px;
  resize: none;
}

.addBtn {
  background-color: transparent;
  border: none;
  display: block;
  margin: 0 auto;
  padding: 4px 8px;
  transition: all 100ms ease;
  border-radius: 15px;
}

.addBtn:hover {
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 10%) inset,
    0 -2px 4px 0 rgba(0, 0, 0, 10%) inset;
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
</style>