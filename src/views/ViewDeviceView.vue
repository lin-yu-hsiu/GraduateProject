<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div
      class="d-flex flex-column p-5 mx-auto w-100"
      style="position: relative"
    >
      <div
        style="
          font-weight: bold;
          font-size: 18px;
          color: rgba(0, 0, 0, 30%);
          align-self: flex-start;
          align-items: center;
        "
      >
        <img
          :src="crumb"
          alt=""
          style="width: 30px; height: 30px; padding-bottom: 5px"
        />
        {{ $store.state.currentvenue }}
        <img
          :src="crumb"
          alt=""
          style="width: 30px; height: 30px; padding-bottom: 5px"
        />
        查看區域
      </div>
      <div class="d-flex align-items-center justify-content-center mx-auto">
        <div
          style="font-weight: bold; font-size: 24px; color: rgba(0, 0, 0, 50%)"
        >
          您目前所在場館為
        </div>
        <div
          style="
            font-weight: 800;
            font-size: 26px;
            color: rgba(0, 0, 0, 90%);
            margin-left: 10px;
          "
        >
          {{ $store.state.currentvenue }}
        </div>
      </div>
      <div class="w-100 d-flex justify-content-end mt-2">
        <div class="editRegion">
          <div class="editMode" v-if="!this.$store.state.openMapFlag">
            編輯模式
            <n-switch
              v-model:value="this.$store.state.deviceEditMode"
              style="margin-left: 10px"
            />
          </div>
        </div>
      </div>
      <div
        v-if="$store.state.currvenue"
        class="d-flex justify-content-center flex-wrap"
        @ifEmpty="ifEmpty_ViewDevice"
      >
        <ViewRegion
          v-for="item in maps"
          :key="item.id"
          :region="item"
          @_reDisplay="reDisplay"
        >
        </ViewRegion>
        <div v-if="this.$store.state.deviceEditMode" class="AddRegion m-3">
          <router-link
            :to="{ name: 'addregion' }"
            style="text-decoration: none"
          >
            <button
              class="AddRegionBtn"
              @mouseover="icon1 = addRegion_icon_blue"
              @mouseleave="icon1 = addRegion_icon"
            >
              <img :src="icon1" style="width: 40px; height: 40px" />
              新增區域
            </button>
          </router-link>
        </div>
      </div>

      <div
        v-if="!mapFlag && !this.$store.state.deviceEditMode"
        style="
          font-weight: bold;
          font-size: 18px;
          color: rgba(0, 0, 0, 50%);
          margin-top: 25vh;
          text-align: center;
        "
      >
        目前
        {{ $store.state.currentvenue }}
        無任何區域，請點擊右上方新增區域此功能
      </div>
      <ViewPic
        v-if="this.$store.state.openPicFlag"
        @close="
          this.$store.state.openPicFlag = false;
          this.$store.state.openPicName = '';
          this.$store.state.openPicRegionName = '';
        "
        style="
          position: absolute;
          top: 0;
          bottom: 0;
          left: 0;
          right: 0;
          margin: auto;
          z-index: 1000;
        "
      >
      </ViewPic>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { inject } from "vue";
import { useMessage } from "naive-ui";
import ViewPic from "@/components/ViewPic.vue";
import MenuBar from "@/components/MenuBar.vue";
import ViewRegion from "@/components/ViewRegion.vue";
import addRegion_icon from "../assets/pic/addRegion_icon.png";
import addRegion_icon_blue from "../assets/pic/addRegion_icon_blue.png";
import crumb from "../assets/pic/crumb.png";

export default {
  setup() {
    const reload = inject("reload");
    const message = useMessage();
    const update = () => {
      reload();
    };
    const mistake = () => {
      message.error("請先關閉地圖");
    };
    return {
      update,
      mistake,
    };
  },
  components: {
    MenuBar,
    ViewRegion,
    ViewPic,
  },
  data() {
    return {
      maps: [],
      mapFlag: false,
      icon1: addRegion_icon,
      addRegion_icon: addRegion_icon,
      addRegion_icon_blue: addRegion_icon_blue,
      crumb: crumb,
      mapOpening: "mapOpening",
    };
  },
  methods: {
    mustCloseMap() {
      if (this.$store.state.openMapFlag) {
        this.mistake();
      }
    },
    async fetchTableMap() {
      let tempmaps = [];
      await axios({
        method: "get",
        baseURL: this.$store.state.api + "/table/Map",
        "Content-Type": "application/json",
      })
        .then((response) => (tempmaps = response.data))
        .catch((err) => {
          console.error(err);
        });

      //尋訪/table/Map中之指定場館中所有區域 ( 包括已經無裝置的區域 )
      for (const key in tempmaps) {
        if (tempmaps[key].Venue == this.$store.state.currentvenue) {
          this.maps.push(tempmaps[key]);
          this.mapFlag = true;
        }
      }
    },
    ifEmpty_ViewDevice() {
      this.fetchTableMap();
      this.update();
    },
    reDisplay() {
      this.maps = [];
      this.fetchTableMap();
      this.update();
    },
  },
  mounted() {
    this.$store.state.deviceEditMode = false;
    this.fetchTableMap();
    if (this.$store.state.currvenue == false) {
      this.$router.push("/");
    }
  },
};
</script>

<style scoped>
.AddRegion {
  width: 270px;
  height: 150px;
  background-color: rgba(142, 142, 142, 100%);
  box-shadow: 0 10px 10px 0 rgba(0, 0, 0, 25%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  border-radius: 20px;
}

.AddRegion:hover {
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 5%) inset;
}

.editRegion {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: center;
  padding: 4px 8px;
}

.editMode {
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: 18px;
  border-radius: 5px;
  box-shadow: 0 0 5px 5px rgba(0, 0, 0, 0.1);
  width: 150px;
  padding: 5px 5px;
  transition: all 0.2s ease;
}

.AddRegionBtn {
  font-weight: bold;
  font-size: 18px;
  border-radius: 5px;
  box-shadow: 0 0 5px 5px rgba(0, 0, 0, 0.1);
  background-color: rgba(0, 0, 0, 0.8);
  color: rgba(255, 255, 255, 0.8);
  width: 150px;
  padding: 5px 5px;
  border: none;
  outline: none;
  display: flex;
  justify-content: space-around;
  align-items: center;
  transition: all 0.2s ease;
}

.AddRegionBtn:hover {
  color: rgba(0, 0, 0, 0.8);
  background-color: rgb(224, 224, 224);
  width: 170px;
}

.RemoveRegion {
  font-weight: bold;
  font-size: 18px;
  border-radius: 5px;
  box-shadow: 0 0 5px 5px rgba(0, 0, 0, 0.1);
  width: 130px;
  padding: 5px 5px;
  border: none;
  outline: none;
  transition: all 0.2s ease;
}

.RemoveRegion:hover {
  background-color: rgba(215, 215, 215, 0.8);
  color: rgba(215, 2, 2, 1);
  width: 155px;
}
</style>
