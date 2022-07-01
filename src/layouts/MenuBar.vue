<template>
  <div class="menu">
    <button class="content">
      <div id="addRegion" class="option">
        <img id="addRegion_icon" src="../assets/icon/addRegion_icon.png" alt="" style="width: 45px; height: 45px">
        <h2 class="function">新增區域</h2>
      </div>
      <div class="decoration"></div>
    </button>
    <button class="content">
      <div id="addDevice" class="option">
        <img id="addDevice_icon" src="../assets/icon/addDevice_icon.png" alt="" style="width: 45px; height: 45px">
        <h2 class="function">新增裝置</h2>
      </div>
      <div class="decoration"></div>
    </button>
    <button class="content">
      <div id="viewDevice" class="option">
        <img id="viewDevice_icon" src="../assets/icon/viewDevice_icon.png" alt="" style="width: 45px; height: 45px">
        <h2 class="function">查看裝置</h2>
      </div>
      <div class="decoration"></div>
    </button>

    <button class="content">
      <div id="switchRegion" class="option">
        <img id="switchRegion_icon" src="../assets/icon/switchRegion_icon.png" alt="" style="width: 45px; height: 45px">
        <h2 class="function">切換區域</h2>
      </div>
      <div class="decoration"></div>
    </button>

    <div class="info">
      <button class="content">
        <div id="setting" class="option">
          <img id="setting_icon" src="../assets/icon/setting_icon.png" alt="" style="width: 45px; height: 45px">
          <h2 class="function">設定</h2>
        </div>
        <div class="decoration"></div>
      </button>

      <button class="content">
        <div id="FAQ" class="option">
          <img id="FAQ_icon" src="../assets/icon/FAQ_icon.png" alt="" style="width: 45px; height: 45px">
          <h2 class="function">FAQ</h2>
        </div>
        <div class="decoration"></div>
      </button>
    </div>
  </div>
</template>


<script>
import $ from 'jquery'


export default {
  name: "MenuBar",
  data() {
    return {

    }
  },
  mounted() {
    let optionName = document.querySelectorAll('.function');
    let menu = document.querySelector('.menu');
    let picId;
    $(document).ready(function () {
      $(menu).hover(function () {
        $(optionName).fadeIn(300)
        $(this).css('width', '190px');
      }, function () {
        $(optionName).hide()
        $(this).css('width', '100px');
      });
      $('.option').hover(function () {
        picId = $(this).find('img').attr('id');
        //用絕對路徑引入時，路徑讀取的是public資料夾中的資源，任何放置在 public 資料夾的靜態資源都會被簡單的複製到編譯後的目錄中，而不經過 webpack特殊處理。
        $('#' + picId).attr("src", "./icon/" + picId + "_blue.png");
        $(this).siblings().css("background-color", "#B6FFFF");
        $(this).css("background-color", "rgba(255, 255, 255, 0.3)");
      }, function () {
        picId = $(this).find('img').attr('id');
        $('#' + picId).attr("src", "./icon/" + picId + ".png");
        $(this).siblings().css("background-color", "transparent");
        $(this).css("background", "transparent");
      });
      $('.decoration').hover(function () {
        $(this).css("background-color", "#B6FFFF");
      }, function () {
        $(this).css("background", "transparent");
      });
    });
  }
}
</script>

<style scoped>
.menu {
  transition: 300ms all ease;
  background: linear-gradient(to right, #434343 0%, black 100%);
  height: 100vh;
  width: 100px;
  padding: 150px 0 20px 0;
  position: relative;
}

.option {
  width: 180px;
  padding: 5px 0 5px 20px;
  display: flex;
  justify-content: start;
  align-items: center;
  transition: 100ms all ease;
}

.content {
  display: flex;
  justify-content: start;
  align-items: center;
  background-color: transparent;
  border: 0;
  padding: 0;
}

.option img {
  width: 60px;
  margin: 0 10px 0 0;
}

.function {
  color: #FFFFFF;
  width: 100px;
  font-size: 20px;
  text-align: center;
  margin: 0;
  display: none;
}

.info {
  width: 100%;
  position: absolute;
  bottom: 0;
}

.decoration {
  transition: 100ms all ease;
  height: 55px;
  width: 10px;
  justify-self: end;
}
</style>