<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="p-5 h-100 w-100 mx-auto">
      <div v-if="!this.$store.state.currvenue"
        style="font-weight: bold; font-size: 24px; color: rgba(0, 0, 0, 70%); text-align: center;">
        請點擊以下欲切換之場館
      </div>
      <div v-else style="font-weight: bold; font-size: 24px; color: rgba(0, 0, 0, 70%); text-align: center;">切換成功 !
      </div>
      <div class="d-flex">
        <SwitchBuilding class="m-3" v-for="item in listvenues" :key="item.id" :region="item"
          @click="$store.commit('switchRegion', item);">
        </SwitchBuilding>
        <div class="AddVenue m-3">
          <div style="font-weight: bold; font-size: 22px; color: rgba(0, 0, 0, 100%); text-align: center;">欲新增之場館名稱
          </div>
          <div class="d-flex justify-content-around">
            <input type="text" name="" id="AddVenueInput">
            <button class="detailBtn p-0" @mouseover="icon = add_hover" @mouseleave="icon = add">
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

const venues = []
export default defineComponent({
  components: {
    MenuBar,
    SwitchBuilding
  },
  data() {
    return {
      regions: venues,
      listvenues: [],
      icon: add,
      add: add,
      add_hover: add_hover,
    };
  },
  methods: {
    async fetchAllRegion() {
      const API = this.$store.state.api + '/deviceInfo'
      const res = await axios.get(API, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      this.regions = res.data;
      for (let i = 0; i < this.regions.length; i++) {
        venues.push({ 'Venue': this.regions[i].Venue, 'Area': this.regions[i].Area })
      }
      const venueSet = new Set();
      for (let i = 0; i < this.regions.length; i++) {
        venueSet.add(venues[i].Venue)
      }
      this.listvenues = venueSet.values()
      let SetToArray = [...this.listvenues];
      SetToArray.sort()
      this.listvenues = SetToArray
    },
  },
  mounted() {
    this.fetchAllRegion()
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