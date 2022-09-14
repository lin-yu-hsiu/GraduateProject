<template>
  <div class="d-flex">
    <MenuBar @click="checkOpenQRcode()"></MenuBar>
    <div class="p-5 w-100 mx-auto d-flex justify-content-center align-items-center flex-column" style="height: 100vh">
      <h1 style="font-weight: bold; color: rgba(0, 0, 0, 30%); ">Welcome !</h1>
      <button @click="openQRcode()" class="generateQRcodeBtn">
        切換
        <div v-if="!this.$store.state.QRcodeFlag">內網 / 外網</div> 
        <div v-if="!this.$store.state.QRcodeNetFlag && this.$store.state.QRcodeFlag">成外網</div>       
        <div v-if="this.$store.state.QRcodeNetFlag && this.$store.state.QRcodeFlag">成內網</div>
      </button>
      <div v-if="this.$store.state.QRcodeFlag" class="decoQRcode">
        <div class="QRcodeTitle">
        目前會場專用
        <div v-if="this.$store.state.QRcodeNetFlag">外網網址</div>       
        <div v-else>內網網址</div>            
      </div>
      <QRcode v-if="this.$store.state.QRcodeFlag" :value="this.$store.state.QRcodeURL" :size="300"></QRcode>
      </div>    
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import { defineComponent } from "vue";
import { useMessage } from 'naive-ui'
import MenuBar from "@/components/MenuBar.vue";
import QRcode from "qrcode.vue";

export default defineComponent({
  setup() {
    const message = useMessage()  
    const mistake = () => {
      message.error('請先切換內 / 外網'),
        { duration: 500 }
    }    
    return {    
      mistake,
    }
  },
  components: {
    MenuBar,
    QRcode
  },
  data(){
    return{
      QRcodeSize: 300,
    }
  },
  methods:{
    openQRcode(){
      this.$store.state.QRcodeFlag = true; 
      this.getURL(this.$store.state.QRcodeNetFlag)
      this.$store.state.QRcodeNetFlag = !this.$store.state.QRcodeNetFlag
    },
    checkOpenQRcode(){
      if (!this.$store.state.QRcodeFlag){
        this.mistake()
      }
    },
    async getURL(flag){
      if (flag){
        this.$store.state.QRcodeURL = 'https://firebasestorage.googleapis.com/v0/b/csie-nuk-692a6.appspot.com/o'
      }
      else {
        this.$store.state.QRcodeURL = (await axios({
          method: 'get',
          baseURL: this.$store.state.api + '/localURL',
        })).data
      }
      console.log(this.$store.state.QRcodeURL)
    }
  },
  mounted() {
    this.$store.state.step = '',
    this.$store.state.currvenue = false,
    this.$store.state.currentvenue = '(需先切換場館)',
    this.$store.state.currentUser = '',
    this.$store.state.venueEditMode = false,
    this.$store.state.allvenues = [],
    this.$store.state.deviceEditMode = false,
    this.$store.state.regionAddName = '',
    this.$store.state.openMapFlag = false,
    this.$store.state.openMapName = '',
    this.$store.state.openPicFlag = false,
    this.$store.state.openPicName = '',
    this.$store.state.openPicRegionName = ''
  }
});
</script>

<style scoped>
.generateQRcodeBtn{
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  font-weight: bold;
  border-radius: 5px;
  padding: 4px 8px;
  outline: none;
  background: rgba(0, 0, 0, 0.2);
  color: rgba(0, 0, 0, 0.8);
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 15%);
  text-align: center;
  width: 180px;
  height: 45px;
  font-size: 18px;
  margin-bottom: 10px;
}
.generateQRcodeBtn:hover {
  background-color: #D9D9D9;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 10%) inset;
  color: #2b2b2b;
}
.QRcodeTitle{
  font-size: 18px;
  font-weight: 600;
  display: flex;
  justify-content: center;
  margin: 10px 0;
}
.decoQRcode{
  border: .5px solid rgba(0,0,0,0.1);
  background-color: #ffffff;
  box-shadow: 0 0 5px 1px rgba(0,0,0,0.15) inset;
  padding: 0 20px 20px 20px;
  border-radius: 5px;
}
</style>
