<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column p-5 w-100">
      <div class="d-flex justify-content-center align-items-center">
        <div style="font-weight: bold; font-size: 24px;color: rgba(0, 0, 0, 50%);">您目前所在場館為 </div>
        <div style="font-weight: 800; font-size: 26px; color: rgba(0, 0, 0, 90%); margin-left: 10px;">
          {{
              $store.state.currentvenue
          }}
        </div>
      </div>
      <div v-if="$store.state.currvenue" class="d-flex">
        <ViewRegion v-for="item in regionamount" :key="item.id" :region="item"></ViewRegion>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import MenuBar from '@/components/MenuBar.vue';
import ViewRegion from '@/components/ViewRegion.vue';


export default {
  components: {
    MenuBar,
    ViewRegion
  },
  data() {
    return {
      regionamount: [],
      regioninfo: [],
      temp: [],
    };
  },
  methods: {
    async fetchApi() {
      let regions = []
      const API = 'http://192.168.0.103:5000/deviceInfo'
      await axios.get(API)
        .then((response) => regions = response.data)
        .catch((error) => console.log(error))

      regions.sort()

      const tempregions = []
      for (let i = 0; i < regions.length; i++) {
        if (regions[i].Venue === this.$store.state.currentvenue) {
          tempregions.push(regions[i])
        }
      }
      const length = []
      length[0] = 0
      this.regionamount.push(tempregions[0])
      let len = 0
      for (let i = 1; i < tempregions.length; i++) {
        if (tempregions[i].Area != this.regionamount[len].Area) {
          this.regionamount.push(tempregions[i])
          len++
          length.push(i)
        }
      }
    },

  },
  mounted() {
    this.fetchApi()
  },
};
</script>