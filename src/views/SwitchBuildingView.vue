<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="p-5 w-100 h-100">
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
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { defineComponent } from "vue";
import MenuBar from '@/components/MenuBar.vue';
import SwitchBuilding from '@/components/SwitchBuilding.vue';


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