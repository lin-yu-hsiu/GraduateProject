<template>
  <div class="menu">
    <div class="logout">
      <router-link :to="{ name: 'login' }">
        <button class="content">
          <div id="login" class="option" style="padding: 5px 0 5px 25px;" @mouseover="icon5 = logout_icon_blue"
            @mouseleave="icon5 = logout_icon">
            <img id="login_icon" :src="icon5" alt="" style="width: 45px; height: 45px; margin: 0;">
            <h2 class="function">登出</h2>
          </div>
          <div class="decoration"></div>
        </button>
      </router-link>
    </div>

    <div style="position: absolute; top: 30vh;">
      <router-link :to="{ name: 'addregion' }">
        <button class="content">
          <div id="addRegion" class="option" @mouseover="icon1 = addRegion_icon_blue"
            @mouseleave="icon1 = addRegion_icon">
            <img id="addRegion_icon" :src="icon1" alt="" style="width: 45px; height: 45px">
            <h2 class="function">新增區域</h2>
          </div>
          <div class="decoration"></div>
        </button>
      </router-link>

      <router-link :to="{ name: 'adddevice' }">
        <button class="content">
          <div id="addDevice" class="option" @mouseover="icon2 = addDevice_icon_blue"
            @mouseleave="icon2 = addDevice_icon">
            <img id="addDevice_icon" :src="icon2" alt="" style="width: 45px; height: 45px">
            <h2 class="function">新增裝置</h2>
          </div>
          <div class="decoration"></div>
        </button>
      </router-link>

      <router-link :to="{ name: 'viewdevice' }">
        <button class="content">
          <div id="viewDevice" class="option" @mouseover="icon3 = viewDevice_icon_blue"
            @mouseleave="icon3 = viewDevice_icon">
            <img id="viewDevice_icon" :src="icon3" alt="" style="width: 45px; height: 45px">
            <h2 class="function">查看裝置</h2>
          </div>
          <div class="decoration"></div>
        </button>
      </router-link>

      <router-link :to="{ name: 'switchregion' }">
        <button class="content">
          <div id="switchRegion" class="option" @mouseover="icon4 = switchRegion_icon_blue"
            @mouseleave="icon4 = switchRegion_icon">
            <img id="switchRegion_icon" :src="icon4" alt="" style="width: 45px; height: 45px">
            <h2 class="function">切換場館</h2>
          </div>
          <div class="decoration"></div>
        </button>
      </router-link>
    </div>



    <div class="info">
      <router-link :to="{ name: 'FAQ' }">
        <button class="content">
          <div id="FAQ" class="option" @mouseover="icon6 = FAQ_icon_blue" @mouseleave="icon6 = FAQ_icon">
            <img id="FAQ_icon" :src="icon6" alt="" style="width: 45px; height: 45px">
            <h2 class="function">FAQ</h2>
          </div>
          <div class="decoration"></div>
        </button>
      </router-link>
    </div>
  </div>
</template>


<script>
import $ from 'jquery'
import addRegion_icon from '../assets/pic/addRegion_icon.png'
import addDevice_icon from '../assets/pic/addDevice_icon.png'
import viewDevice_icon from '../assets/pic/viewDevice_icon.png'
import switchRegion_icon from '../assets/pic/switchRegion_icon.png'
import FAQ_icon from '../assets/pic/FAQ_icon.png'
import logout_icon from '../assets/pic/logout_icon.png'


import addRegion_icon_blue from '../assets/pic/addRegion_icon_blue.png'
import addDevice_icon_blue from '../assets/pic/addDevice_icon_blue.png'
import viewDevice_icon_blue from '../assets/pic/viewDevice_icon_blue.png'
import switchRegion_icon_blue from '../assets/pic/switchRegion_icon_blue.png'
import FAQ_icon_blue from '../assets/pic/FAQ_icon_blue.png'
import logout_icon_blue from '../assets/pic/logout_icon_blue.png'


export default {
  name: "MenuBar",
  data() {
    return {
      icon1: addRegion_icon,
      icon2: addDevice_icon,
      icon3: viewDevice_icon,
      icon4: switchRegion_icon,
      icon5: logout_icon,
      icon6: FAQ_icon,
      addRegion_icon: addRegion_icon,
      addDevice_icon: addDevice_icon,
      viewDevice_icon: viewDevice_icon,
      switchRegion_icon: switchRegion_icon,
      logout_icon: logout_icon,
      FAQ_icon: FAQ_icon,
      addRegion_icon_blue: addRegion_icon_blue,
      addDevice_icon_blue: addDevice_icon_blue,
      viewDevice_icon_blue: viewDevice_icon_blue,
      switchRegion_icon_blue: switchRegion_icon_blue,
      logout_icon_blue: logout_icon_blue,
      FAQ_icon_blue: FAQ_icon_blue
    }
  },
  mounted() {
    let optionName = document.querySelectorAll('.function');
    let menu = document.querySelector('.menu');
    $(document).ready(function () {
      $(menu).hover(function () {
        $(optionName).fadeIn(200)
        $(this).css('width', '200px');
      }, function () {
        $(optionName).fadeOut(200)
        $(this).css('width', '100px');
      });
      $('.option').hover(function () {
        $(this).siblings().css("background-color", "#B6FFFF");
        $(this).css("background-color", "rgba(255, 255, 255, 0.3)");
      }, function () {
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
a {
  text-decoration: none;
}

.menu {
  transition: 250ms all ease;
  /* background: linear-gradient(to right, #434343 0%, black 100%); */
  background: linear-gradient(to left, transparent 0%, #505050 1%, black 100%);
  height: 100vh;
  width: 100px;
  position: relative;
}

.info {
  position: absolute;
  bottom: 25px;
  width: 100%
}

.logout {
  position: absolute;
  top: 25px;
  width: 100%
}

.option {
  padding: 5px 0 5px 20px;
  display: flex;
  justify-content: start;
  align-items: center;
  transition: 200ms all ease;
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
  margin: 0 5px 0 0;
}

.function {
  color: #FFFFFF;
  width: 95px;
  font-size: 20px;
  text-align: center;
  margin: 0;
  display: none;
  font-weight: bold;
}

.decoration {
  transition: 100ms all ease;
  height: 55px;
  width: 5px;
  justify-self: end;
}
</style>