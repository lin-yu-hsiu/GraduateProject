<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex p-5 w-100">
      <SwitchBuilding class="m-3" v-for="item in listvenues" :key="item.id" :region="item"
        @click="$store.commit('switchRegion', item)">
      </SwitchBuilding>
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
      listvenues: []
    };
  },
  methods: {
    async fetchAllRegion() {

      const API = 'http://192.168.0.103:5000/deviceInfo'
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
    },
  },
  mounted() {
    this.fetchAllRegion()
  }
});
</script>