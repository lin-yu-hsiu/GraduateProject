<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column p-5 w-100 mx-auto" style="max-height: 100vh">
      <div style="font-weight: bold; font-size: 18px;color: rgba(0, 0, 0, 30%);">
        /
        {{
            $store.state.currentvenue
        }}
        / 新增區域
      </div>
      <div class="d-flex justify-content-center align-items-center">
        <div style="font-weight: bold; font-size: 24px;color: rgba(0, 0, 0, 50%);">您目前所在場館為 </div>
        <div style="font-weight: 800; font-size: 26px; color: rgba(0, 0, 0, 90%); margin-left: 10px;">
          {{
              $store.state.currentvenue
          }}
        </div>
      </div>
      <div v-if="$store.state.currvenue" class="d-flex justify-content-center align-items-center my-5">
        <div class="title mx-3">
          區域名稱
        </div>
        <input v-model="regionName" id="RegionName" class="regionName" type="text" placeholder="欲新增之區域名稱">
      </div>
      <div v-if="$store.state.currvenue" class="picRegion d-flex flex-column justify-content-center align-items-center">
        <img :src="previewImage" style="max-width: 98%; max-height: 70%; border-radius: 5px; margin-bottom: 20px;">
        <input type="file" accept="image/*" style="display: none;" @change="onFileChanged" ref="fileInput">
        <button class="clickToLoad" @click="$refs.fileInput.click()">
          <img :src="loadpic" style="width: 45px; height: 45px">
          {{ pic }}
        </button>
        <n-modal v-model:show="showModal">
          <n-card style="width: 300px; text-align: center; font-weight: bold;" title="新增失敗" size="huge" role="dialog"
            aria-modal="true">
            資料尚未填齊
          </n-card>
        </n-modal>
      </div>
      <button v-if="$store.state.currvenue" class="clickToStore" @click="onUpload">
        <img :src="store_black" style="width: 45px; height: 55px">
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { defineComponent, ref } from "vue";
// import { useStore } from "vuex";
import MenuBar from '@/components/MenuBar.vue';
import loadpic from '../assets/pic/loadpic.png'
import store_black from '../assets/pic/store_black.png'


export default defineComponent({
  setup() {
    return {
      showModal: ref(false)
    };
  },
  components: {
    MenuBar,
  },
  data() {
    return {
      store_black: store_black,
      loadpic: loadpic,
      selectedFile: null,
      regionName: '',
      pic: '點擊以匯入平面圖 ...',
      previewImage: undefined
    };
  },
  methods: {
    onFileChanged(event) {
      this.selectedFile = event.target.files[0]
      this.pic = this.selectedFile.name
      this.previewImage = URL.createObjectURL(this.selectedFile);
    },
    async onUpload() {
      if (this.selectedFile == null || this.regionName == null) {
        this.showModal = true
        return;
      }
      let body = {
        'Route': this.selectedFile.name,
        'Venue': this.$store.state.currentvenue,
        'Area': this.regionName,
      }
      const json = JSON.stringify(body)
      let res = []
      await axios({
        method: 'post',
        url: this.$store.state.api + '/insertArea',
        headers: { 'Content-Type': 'application/json' },
        data: json,
        onUploadProgress: uploadEvent => {
          console.log('Upload Progress: ' + Math.round(uploadEvent.loaded / uploadEvent.total * 100) + '%')
        }
      }).then((response) => res = response.data)
        .catch((err) => { console.error(err) })
      console.log(res)
    }
  },

});
</script>

<style scoped>
.picRegion {
  width: 70vw;
  height: 60%;
  max-width: 1500px;
  background-color: #D9D9D9;
  box-shadow: 0 0 30px 0 rgba(0, 0, 0, 25%) inset;
  margin: 0 auto;
  position: relative;
}

.title {
  font-size: 24px;
  font-weight: 800;
  border-radius: 20px;
  text-align: center;
  background-color: #ffffff;
  width: 150px;
  height: 45px;
  line-height: 2;
}

.regionName {
  border-radius: 20px;
  font-size: 18px;
  text-align: center;
  font-weight: 500;
  background-color: #ffffff;
  outline: none;
  border: none;
  width: 200px;
  height: 40px;
}

.clickToLoad {
  border: none;
  font-weight: bold;
  border-radius: 5px;
  padding: 4px 8px;
  outline: none;
  background: linear-gradient(to right, #ffffff 0%, #D9D9D9 100%);
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 15%);
  text-align: center;
  width: auto;
  margin: 0 auto;
}

.clickToLoad:hover {
  background-color: #D9D9D9;
  box-shadow: 0 0 20px 0 rgba(0, 0, 0, 10%) inset;
  color: #2b2b2b;
}

.clickToStore {
  background-color: transparent;
  border: none;
  margin: 30px auto;
  padding: 4px 8px;
  transition: all 100ms ease;
  border-radius: 15px;
}

.clickToStore:hover {
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 15%) inset,
    0 -2px 4px 0 rgba(0, 0, 0, 15%) inset;
}
</style>