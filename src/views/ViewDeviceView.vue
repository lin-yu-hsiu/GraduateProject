<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex p-5 w-100" style="position: relative;">
      <ViewRegion v-for="item in regionamount" :key="item.id" :region="item"></ViewRegion>
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
      const API = 'http://192.168.0.102:5000/deviceInfo'
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