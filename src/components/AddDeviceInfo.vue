<template>
  <n-card hoverable closable class="checkDevice">
    <h3 class="text-center mb-5" style="font-weight: bold;">欲新增裝置之必填資料
    </h3>
    <div class="d-flex justify-content-between mx-auto mb-2" style="width: 300px">
      <div class="subTitle">裝置編號</div>
      <n-select @change="onChangeMethod($event)" size="medium" :consistent-menu-width="true" v-model:show="show"
        v-model:value="BLEUUID" filterable placeholder="選擇欲配對之裝置" :options="options" id="selectBar">
        <template v-if="show" #arrow>
          <md-search />
        </template>
      </n-select>
    </div>
    <div class="d-flex justify-content-between mx-auto mb-2" style="width: 300px">
      <div class="subTitle">裝置區域</div>
      <div class="edit" disabled style="color: #FFFFFF; background-color: rgba(0, 0, 0, 0.5);cursor: not-allowed"
        v-if="info[0].Area != null">{{ info[0].Area }}</div>
      <div class="edit" style="color: rgba(255, 255, 255, 0.65); background-color: rgba(0, 0, 0, 0.5);" v-else>尚未選取區域
      </div>
    </div>
    <div class="d-flex justify-content-between mx-auto" style="width: 300px">
      <div class="subTitle">標題</div>
      <input v-model="titlevalue" class="edit" type="text">
    </div>
    <div class="d-flex justify-content-between align-items-center mx-auto" style="width: 300px;">
      <div class="subTitle my-4" style="align-self: flex-start">訊息內容</div>
      <div class="d-flex justify-content-around align-items-center"
        style="background-color: rgba(217, 217, 217, 40%); width: 180px; padding: 2px; border-radius: 5px;">
        <n-tooltip trigger="hover">
          <template #trigger>
            <img :src="icon1" @mouseover="icon1 = txt_hover" @mouseleave="icon1 = txt"
              @click="messageTextStatus = !messageTextStatus">
          </template>
          文字
        </n-tooltip>
        <n-tooltip trigger="hover">
          <template #trigger>
            <img :src="icon2" @mouseover="icon2 = voice_hover" @mouseleave="icon2 = voice"
              @click="messageAudioStatus = !messageAudioStatus; this.$refs.messagevoice.click(); ">
          </template>
          音檔
        </n-tooltip>
        <n-tooltip trigger="hover">
          <template #trigger>
            <img :src="icon3" @mouseover="icon3 = link_hover" @mouseleave="icon3 = link"
              @click="messageLinkStatus = !messageLinkStatus">
          </template>
          連結
        </n-tooltip>
      </div>
    </div>
    <div class="mx-auto" style="width: 300px;">
      <textarea v-if="messageTextStatus == true" v-model="BLEMessage" class="message scroll p-3"
        placeholder="請輸入文字內容"></textarea>
      <div v-if="messageAudioStatus == true" style=" background-color: rgba(217, 217, 217, 50%); padding: 4px 8px; margin: 0 auto; text-align:center;
         font-weight: 800; font-size: 16px;margin-bottom: 8px;">
        檔案名稱 : {{ voicename }}
      </div>
      <textarea v-if="messageLinkStatus == true" v-model="BLEHref" class="message scroll p-3"
        placeholder="請輸入網址"></textarea>
      <div v-if="messageAudioStatus == false">
        <input type="file" accept="audio/*" style="display: none;" ref="messagevoice" @change="UploadMessageVoice">
      </div>
    </div>
    <button @click="sendToAddDevice();" class="addBtn mt-5">
      <div>Save</div>
    </button>
  </n-card>
</template>

<script>
import axios from 'axios'
import { defineComponent, inject, ref } from 'vue'
import { useMessage } from 'naive-ui'
import MdSearch from '@vicons/ionicons4/MdSearch'
import ok from '../assets/pic/ok.png'
import txt from '../assets/pic/txt.png'
import txt_hover from '../assets/pic/txt_hover.png'
import voice from '../assets/pic/voice.png'
import voice_hover from '../assets/pic/voice_hover.png'
import link from '../assets/pic/link.png'
import link_hover from '../assets/pic/link_hover.png'


export default defineComponent({
  setup() {
    const reload = inject('reload')
    const message = useMessage()
    const update = () => {
      message.success('新增成功'),
        { duration: 500 }
    }
    const mistake = () => {
      message.error('新增失敗\n資料尚未填齊'),
        { duration: 500 }
    }
    const uploadAudioFail = () => {
      message.error('音檔上傳失敗'),
        { duration: 500 }
    }
    return {
      show: ref(false),
      options: [],
      update,
      mistake,
      uploadAudioFail,
      reload
    }
  },
  components: {
    MdSearch,
  },
  props: {
    info: {
      type: Object,
    }
  },
  data() {
    return {
      BLEUUID: null,
      device: this.info,
      titlevalue: '',
      BLEMessage: '',
      BLEHref: '',
      messageLinkStatus: false,
      messageTextStatus: false,
      messageAudioStatus: false,
      messageContent: '',
      connectSuccess: true,
      disableBtn: true,
      selectedVoice: null,
      voicename: '',
      //
      ok: ok,
      txt: txt,
      txt_hover: txt_hover,
      voice: voice,
      voice_hover: voice_hover,
      link: link,
      link_hover: link_hover,
      icon1: txt,
      icon2: voice,
      icon3: link,
    }
  },
  methods: {
    UploadMessageVoice(event) {
      this.selectedVoice = event.target.files[0]
      this.voicename = this.selectedVoice.name
      this.messageContent = 'voice'
    },
    onChangeMethod(event) {
      this.BLEUUID = event
    },
    async fetchUUID() {
      let UUIDs
      await axios({
        method: 'get',
        baseURL: this.$store.state.api + '/newDevice',
        'Content-Type': 'application/json',
      })
        .then((response) => UUIDs = response.data)
        .catch((err) => { console.error(err) })

      if (UUIDs['free'].length != 0) {
        for (let i = 0; i < UUIDs['free'].length; i++) {
          this.options.push({ 'label': UUIDs['free'][i], 'value': UUIDs['free'][i] })
        }
      }
      else {
        return
      }
    },
    async sendToAddDevice() {
      if (this.titlevalue == '' || this.BLEUUID == null) {
        this.mistake()
        return
      }
      else {
        let audioFlag = 0
        if (this.selectedVoice != null) {
          let fileName = this.$store.state.currentvenue + '_' + this.info[0].Area + '_' + this.titlevalue + '.mp3'
          let uploadFile = this.selectedVoice
          let formData = new FormData()
          formData.append('file', uploadFile, fileName)
          let res = []
          await axios({
            method: 'post',
            url: this.$store.state.api + '/uploadAud',
            headers: { "Content-Type": "multipart/form-data" },
            data: formData,
          }).then((response) => res = response.data)
            .catch((err) => { console.error(err) })
          console.log(res)
          if (res.success == 0) {
            audioFlag = 0
            this.uploadAudioFail()
          }
          else {
            audioFlag = 1
          }
        }
        let body = {
          'UUID': this.BLEUUID,
          'Title': this.titlevalue,
          'Message': this.BLEMessage,
          'Href': this.BLEHref,
          'Audio': audioFlag
        }
        let temp = Object.assign({}, this.device[0], body) //合併兩個物件
        const json = JSON.stringify(temp);
        let res
        await axios({
          method: 'post',
          baseURL: this.$store.state.api + '/insertBLE',
          headers: { 'Content-Type': 'application/json' },
          data: json
        })
          .then((response) => res = response.data)
          .catch((error) => console.log(error))
        // console.log(res)
        if (res.success == 1) {
          this.update()
          this.$emit('AddSuccess', this.device[0].Area)
        }
        else {
          this.mistake()
        }
      }
    }
  },
  mounted() {
    this.fetchUUID()
  }
})
</script>


<style scoped>
#selectBar {
  width: 180px;
  text-align: center;
}

.checkDevice {
  width: 500px;
  background-color: #ffffff;
  border-radius: 15px;
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 25%),
    0 -4px 20px 0 rgba(0, 0, 0, 25%);
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}

.subTitle {
  width: 100px;
  height: 30px;
  background-color: rgba(201, 201, 201, 80%);
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 25%);
  font-weight: bold;
  font-size: 18px;
  text-align: center;
  line-height: 1.8;
}

.message {
  background-color: rgba(217, 217, 217, 50%);
  width: 300px;
  height: 80px;
  border: none;
  outline: none;
  padding: 8px;
  resize: none;
  font-size: 16px;
  cursor: auto;
}

.edit {
  outline: none;
  border: solid .5px rgba(0, 0, 0, 15%);
  padding: 4px 8px;
  font-size: 16px;
  font-weight: 500;
  text-align: center;
  border-radius: 5px;
  resize: none;
  color: #000000;
  background-color: rgba(217, 217, 217, 50%);
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 15%);
  width: 180px;
}

.addBtn {
  background-color: rgba(0, 0, 0, 0.8);
  border: 0.5px solid rgb(185, 185, 185);
  display: block;
  margin: 0 auto;
  padding: 4px 30px;
  transition: all 100ms ease;
  border-radius: 5px;
  color: rgba(0, 0, 0, 1);
  font-size: 18px;
  font-weight: 600;
  background-color: rgba(201, 201, 201, 100%);
  box-shadow: 0 0 4px 0 rgba(0, 0, 0, 15%);
}

.addBtn:hover {
  background-color: rgba(201, 201, 201, 80%)
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