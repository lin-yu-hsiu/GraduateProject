<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column p-5 w-100 mx-auto" style="max-height: 100vh">
      <div style="font-weight: bold; font-size: 18px;color: rgba(0, 0, 0, 30%);">
        /
        {{
            this.$store.state.currentvenue
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
      <div v-if="this.$store.state.currvenue" class="d-flex justify-content-center align-items-center my-5">
        <div class="title mx-3">
          區域名稱
        </div>
        <input v-model="regionName" id="RegionName" class="regionName" type="text" placeholder="欲新增之區域名稱">
      </div>
      <div v-if="$store.state.currvenue" class="picRegion d-flex flex-column justify-content-center align-items-center">
        <img :src="previewImage" style="max-width: 98%; max-height: 70%; border-radius: 5px; margin-bottom: 20px;">
        <button class="clickToLoad" @click="this.$refs.regionimage.click()">
          <img :src="loadpic" style="width: 45px; height: 45px">
          {{ pic }}
        </button>
        <input type="file" accept="image/*" style="display: none;" ref="regionimage" @change="UploadImage">
      </div>
      <button v-if="$store.state.currvenue" class="clickToStore" @click="UploadData">
        <img :src="store_black" style="width: 45px; height: 55px">
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import { defineComponent } from "vue";
import { defineComponent, inject } from "vue";
import { useMessage } from 'naive-ui'
import MenuBar from '@/components/MenuBar.vue';
import loadpic from '../assets/pic/loadpic.png'
import store_black from '../assets/pic/store_black.png'


export default defineComponent({
  setup() {
    const reload = inject('reload')
    const message = useMessage()
    const update = () => {
      message.success('新增成功'),
        { duration: 1000 }
      reload()
    }
    const mistake = () => {
      message.error('尚未載入平面圖'),
        { duration: 1000 }
      reload()
    }
    const already = () => {
      message.error('已新增過相同名稱之區域'),
        { duration: 1000 }
      reload()
    }
    const noname = () => {
      message.error('請先填寫區域名稱'),
        { duration: 1000 }
      reload()
    }
    return {
      update,
      mistake,
      already,
      noname
    }
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
      previewImage: undefined,
      sendFlag: false
    };
  },
  methods: {
    async UploadImage(event) {
      if (this.regionName == '') {
        this.noname()
      }
      else {
        event.preventDefault();
        this.selectedFile = event.target.files[0]
        // console.log(this.selectedFile)
        this.pic = this.selectedFile.name
        this.previewImage = URL.createObjectURL(this.selectedFile);
        let res1 = []
        await axios({
          method: 'get',
          url: this.$store.state.api + '/table/' + this.$store.state.currentvenue,
          headers: { "Content-Type": 'application/json' },
        }).then((response) => res1 = response.data)
          .catch((err) => { console.error(err) })

        if (this.regionName != '') {
          for (let i = 0; i < Object.values(res1).length; i++) {
            if (this.regionName == res1[i].Area) {
              this.already()
              this.sendFlag = true
              return
            }
          }
        }
        let formData = new FormData()
        let imgName = this.$store.state.currentvenue + "_" + this.regionName + '.jpg'
        formData.append('file', this.selectedFile, imgName)

        let res = []
        await axios({
          method: 'post',
          url: this.$store.state.api + '/uploadPic',
          headers: { "Content-Type": "image/png" },
          data: formData,
        }).then((response) => res = response.data)
          .catch((err) => { console.error(err) })
        console.log(res)
      }
    },
    async UploadData() {
      if (this.selectedFile == null) {
        this.mistake()
      }

      if (this.regionName == '') {
        this.mistake()
        this.sendFlag = true
      }
      if (this.sendFlag === false && this.selectedFile != null) {
        let body = {
          'Venue': this.$store.state.currentvenue,
          'Area': this.regionName,
          'fileName': this.$store.state.currentvenue + '_' + this.regionName + '.jpg'
        }
        let res = []
        await axios({
          method: 'post',
          url: this.$store.state.api + '/insertArea',
          headers: { "Content-Type": 'application/json' },
          data: JSON.stringify(body)
        }).then((response) => res = response.data)
          .catch((err) => { console.error(err) })
        // console.log(res)
        console.log(this.$store.state.currentvenue)
        if (res.success == 1) {
          this.update()
        } else {
          this.mistake()
        }
      }
    },
  },
  mounted() {
    console.log(this.$store.state.currentvenue)
    if (this.$store.state.currvenue == false) {
      console.log(this.$store.state.currentvenue)
      this.$router.push('/')
    }
  }
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
  border-radius: 5px;
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