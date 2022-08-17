<template>
  <div class="menu">
    <div class="logout w-100">
      <router-link :to="{ name: 'login' }">
        <button class="content">
          <div id="login" style="margin: 0 auto;" @mouseover="icon5 = logout_icon_blue"
            @mouseleave="icon5 = logout_icon">
            <n-tooltip placement="right" trigger="hover">
              <template #trigger>
                <img id="login_icon" :src="icon5" alt="" style="display: block; width: 40px; height: 40px;">
              </template>
              登出
            </n-tooltip>
          </div>
        </button>
      </router-link>
    </div>

    <div class="w-100" style="margin: 0 0 20vh 0">
      <router-link :to="{ name: 'switchregion' }">
        <button class="content" @click="this.$store.commit('switchVenue');">
          <div v-if="this.$store.state.step == 'switch'" class="decoration"></div>
          <div id="switchRegion" style="margin: 0 auto;" @mouseover="icon4 = switchRegion_icon_blue"
            @mouseleave="icon4 = switchRegion_icon">
            <n-tooltip placement="right" trigger="hover">
              <template #trigger>
                <img id="switchRegion_icon" :src="icon4" alt="" style="display: block; width: 45px; height: 45px;">
              </template>
              切換場館
            </n-tooltip>
          </div>
        </button>
      </router-link>

      <router-link :to="{ name: 'viewdevice' }" v-show="this.$store.state.currvenue">
        <button class="content" @click="this.$store.commit('viewDevice');">
          <div v-if="this.$store.state.step == 'view'" class="decoration"></div>
          <div id="viewDevice" style="margin: 0 auto;" @mouseover="icon3 = viewDevice_icon_blue"
            @mouseleave="icon3 = viewDevice_icon">
            <n-tooltip placement="right" trigger="hover">
              <template #trigger>
                <img id="viewDevice_icon" :src="icon3" alt="" style="display: block; width: 45px; height: 45px">
              </template>
              查看區域
            </n-tooltip>
          </div>
        </button>
      </router-link>
    </div>

    <div class="info w-100">
      <router-link :to="{ name: 'FAQ' }">
        <button class="content" @click="this.$store.commit('FAQ');">
          <div v-if="this.$store.state.step == 'faq'" class="decoration"></div>
          <div id="FAQ" class="option" style="margin: 0 auto;" @mouseover="icon6 = FAQ_icon_blue"
            @mouseleave="icon6 = FAQ_icon">
            <n-tooltip placement="right" trigger="hover">
              <template #trigger>
                <img id="FAQ_icon" :src="icon6" alt="" style="width: 45px; height: 45px">
              </template>
              FAQ
            </n-tooltip>
          </div>
        </button>
      </router-link>
    </div>
  </div>
</template>


<script>
import viewDevice_icon from '../assets/pic/viewDevice_icon.png'
import switchRegion_icon from '../assets/pic/switchRegion_icon.png'
import FAQ_icon from '../assets/pic/FAQ_icon.png'
import logout_icon from '../assets/pic/logout_icon.png'
import viewDevice_icon_blue from '../assets/pic/viewDevice_icon_blue.png'
import switchRegion_icon_blue from '../assets/pic/switchRegion_icon_blue.png'
import FAQ_icon_blue from '../assets/pic/FAQ_icon_blue.png'
import logout_icon_blue from '../assets/pic/logout_icon_blue.png'


export default {
  name: "MenuBar",
  data() {
    return {
      icon3: viewDevice_icon,
      icon4: switchRegion_icon,
      icon5: logout_icon,
      icon6: FAQ_icon,
      viewDevice_icon: viewDevice_icon,
      switchRegion_icon: switchRegion_icon,
      logout_icon: logout_icon,
      FAQ_icon: FAQ_icon,
      viewDevice_icon_blue: viewDevice_icon_blue,
      switchRegion_icon_blue: switchRegion_icon_blue,
      logout_icon_blue: logout_icon_blue,
      FAQ_icon_blue: FAQ_icon_blue,
    }
  },
}
</script>

<style scoped>
a {
  text-decoration: none;
}

.menu {
  transition: 250ms all ease;
  background: linear-gradient(to bottom, #323232 0%, #3F3F3F 40%, #1C1C1C 150%), linear-gradient(to top, rgba(255, 255, 255, 0.40) 0%, rgba(0, 0, 0, 0.25) 200%);
  background-blend-mode: multiply;
  min-height: 100vh;
  width: 100px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 25px 0;
}



.content {
  display: flex;
  align-items: center;
  background-color: transparent;
  border: 0;
  padding: 0;
  width: 100%;
  position: relative;
  margin: 10px 0;
}

.decoration {
  height: 55px;
  width: 3px;
  background-color: aliceblue;
  position: absolute;
  left: 0;
}
</style>