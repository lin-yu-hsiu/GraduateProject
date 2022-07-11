<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column align-items-center p-5 w-100" style="position: relative">
      <button class="locateBtn mb-3">
        <img :src="locatePic">
      </button>
      <div class="frame">
        <img :src="pic">
      </div>
      <div class="checkDevice p-5">
        <h3 class="text-center mb-5" style="font-weight: bold">欲新增裝置之必填資料</h3>
        <div class="d-flex justify-content-between mx-auto" style="width: 300px">
          <div class="subTitle">裝置編號</div>
          <div class="subTitle" disabled>1</div>
        </div>
        <div class="d-flex flex-column mx-auto align-items-center" style="width: 300px;height: 200px">
          <div class="subTitle my-4" style="align-self: flex-start">訊息內容</div>
          <textarea class="message p-3"></textarea>
        </div>

        <button class="addBtn">
          <img id='addBtn' :src="store_black">
        </button>
        <div class="d-flex justify-content-center align-items-center mt-3" style="font-weight: 800;">
          <img :src="ok" class="me-3" style="width:30px; height:30px">
          確認此裝置已連上網
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue';
import locatePic from '../assets/pic/location.png'
import file from '../assets/pic/file.png'
import mic from '../assets/pic/mic.png'
import txt from '../assets/pic/txt.png'
import ok from '../assets/pic/ok.png'
import store_black from '../assets/pic/store_black.png'
import store_white from '../assets/pic/store_white.png'


import testpic2 from '../assets/pic/2.jpg'

export default {
  components: {
    MenuBar,
  },
  data() {
    return {
      locatePic: locatePic,
      pic: testpic2,
      file: file,
      mic: mic,
      txt: txt,
      ok: ok,
      store_black: store_black,
      store_white: store_white
    };
  },
};
</script>

<style scoped>
.locateBtn {
  border: none;
  background-color: transparent;
  width: 65px;
  height: 70px;
  border-radius: 15px;
  display: flex;
  justify-content: center;
  align-items: center;
  align-self: flex-start;
}

.locateBtn:focus {
  background-color: rgba(0, 0, 0, 75%);
}

.frame {
  width: 80vw;
  height: 700px;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 25%) inset;
  padding: 8px;
  position: relative;
}

.frame img {
  max-height: 100%;
  max-width: 100%;
  width: auto;
  height: auto;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
}

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
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 10%), 0 -1px 4px 0 rgba(0, 0, 0, 10%);
}

.addBtn:hover {
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 10%) inset,
    0 -2px 4px 0 rgba(0, 0, 0, 10%) inset;
}
</style>