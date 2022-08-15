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
      <div class="edit" disabled style="color: #FFFFFF;
  background-color: rgba(0, 0, 0, 0.5);cursor: not-allowed" v-if="info[0].Area != null">{{ info[0].Area }}</div>
      <div class="edit" style="color: rgba(255, 255, 255, 0.65);
  background-color: rgba(0, 0, 0, 0.5);" v-else>尚未選取區域</div>
    </div>
    <div class="d-flex justify-content-between mx-auto" style="width: 300px">
      <div class="subTitle">裝置地點</div>
      <input v-model="placevalue" class="edit" type="text">
    </div>
    <div class="d-flex flex-column mx-auto align-items-center" style="width: 300px;height: 200px">
      <div class="subTitle my-4" style="align-self: flex-start">訊息內容</div>
      <textarea v-model="messagecontent" class="message scroll p-3"></textarea>
    </div>
    <button @click="sendToAddDevice();" class="addBtn mt-5">
      <img v-if="disableBtn" :src="store_black" style="width: 45px; height: 55px">
      <img v-if="!disableBtn && !connectSuccess" :src="store_red" style="width: 45px; height: 55px">
    </button>
  </n-card>
</template>

<script>
import axios from 'axios'
import { defineComponent, inject, ref } from 'vue'
import { useMessage } from 'naive-ui'
import MdSearch from '@vicons/ionicons4/MdSearch'
import ok from '../assets/pic/ok.png'
import store_black from '../assets/pic/store_black.png'
import store_green from '../assets/pic/store_green.png'
import store_red from '../assets/pic/store_red.png'


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
      message.error('新增失敗\n資料尚未填齊'),
        { duration: 1000 }
    }
    return {
      show: ref(false),
      options: [],
      update,
      mistake,
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
      placevalue: '',
      messagecontent: '',
      connectSuccess: true,
      disableBtn: true,
      //
      ok: ok,
      store_black: store_black,
      store_green: store_green,
      store_red: store_red,
    }
  },
  methods: {
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
      if (this.placevalue == '' || this.messagecontent == '') {
        this.mistake()
      }
      else {
        let body = {
          'UUID': this.BLEUUID,
          'Place': this.placevalue,
          'Message': this.messagecontent
        }
        let temp = Object.assign({}, this.device[0], body) //合併兩個物件
        const json = JSON.stringify(temp);
        // console.log(json)
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
  /* height: 600px; */
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
  height: 100px;
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