<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="p-5 h-100 w-100 mx-auto">
      <div style="font-weight: bold; font-size: 18px;color: rgba(0, 0, 0, 30%); align-self: flex-start;">
        /
        {{
            $store.state.currentvenue
        }}
      </div>
      <div v-if="!this.$store.state.currvenue"
        style="font-weight: bold; font-size: 24px; color: rgba(0, 0, 0, 70%); text-align: center;">
        請雙擊以下欲切換之場館
      </div>
      <div v-else style="font-weight: bold; font-size: 24px; color: rgba(0, 0, 0, 70%); text-align: center;">切換成功 !
        您目前所在場館為 {{ $store.state.currentvenue }}
      </div>
      <div class="d-flex justify-content-center" style="flex-wrap: wrap">
        <SwitchBuilding class="m-3" v-for="item in venues" :key="item.id" :region="item" @removeDisplay="reDisplay"
          @dblclick="$store.commit('switchRegion', item);">
        </SwitchBuilding>
        <div class="AddVenue m-3">
          <div style="font-weight: bold; font-size: 22px; color: rgba(0, 0, 0, 100%); text-align: center;">欲新增之場館名稱
          </div>
          <div class="d-flex justify-content-around">
            <input type="text" name="" id="AddVenueInput" v-model="venuedata.name">
            <button class="detailBtn p-0" @click="sendToAddVenue" @mouseover="icon = add_hover"
              @mouseleave="icon = add">
              <img :src="icon" style="width: 50px; height: 50px">
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent } from "vue";
import MenuBar from '@/components/MenuBar.vue';
import SwitchBuilding from '@/components/SwitchBuilding.vue';
import add from '../assets/pic/add.png'
import add_hover from '../assets/pic/add_hover.png'



export default defineComponent({
  components: {
    MenuBar,
    SwitchBuilding
  },
  data() {
    return {
      venues: [],
      venuedata: {
        name: ''
      },
      removingflag: false,

      icon: add,
      add: add,
      add_hover: add_hover,
    };
  },
  methods: {
    async fetchAllVenues() {
      let tempmaps = []
      await axios({
        method: 'get',
        baseURL: this.$store.state.api + '/showVenue',
        'Content-Type': 'application/json',
      })
        .then((response) => tempmaps = response.data)
        .catch((err) => { console.error(err) })
      const venueSet = new Set();
      for (let i = 0; i < tempmaps['場館'].length; i++) {
        venueSet.add(tempmaps['場館'][i])
      }

      let SetToArray = [...venueSet];    // Set 轉成 Array
      SetToArray.sort()
      this.venues = SetToArray
    },
    reDisplay(toRemoveVenue, flag) {
      this.removingflag = flag
      var toRemove = toRemoveVenue;
      var arr = this.venues;
      arr = arr.filter(function (item) {
        return item !== toRemove
      });
      this.venues = arr
      window.location.reload()
    },
    async sendToAddVenue() {
      if (this.venuedata.name != '') {
        let body = {
          'Venue': this.venuedata.name,
        }
        const json = JSON.stringify(body);
        await axios({
          method: 'post',
          url: this.$store.state.api + '/createVenue',
          headers: { 'Content-Type': 'application/json' },
          data: json
        }).then((response) => response = response.data)
          .catch((err) => { console.error(err) })

        this.venuedata.name = ''  //清空輸入格
        this.fetchAllVenues()
        window.location.reload()
      }
    },
  },
  mounted() {
    this.fetchAllVenues()
  }
});
</script>

<style scoped>
.AddVenue {
  width: 320px;
  height: 200px;
  background: linear-gradient(to bottom, #ffffff 0%, rgba(142, 142, 142, 50%) 100%);
  box-shadow: 0 10px 10px 0 rgba(0, 0, 0, 25%);
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  border-radius: 0 0 20px 20px;
  padding: 20px;
}

.AddVenue:hover {
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 5%) inset;
}

#AddVenueInput {
  outline: none;
  border: none;
  padding: 4px 8px;
  font-weight: bold;
  font-size: 20px;
  width: 180px;
  border-radius: 5px;
}

.detailBtn {
  background-color: transparent;
  border: none;
}
</style>