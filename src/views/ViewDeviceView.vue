<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column p-5 mx-auto w-100">
      <div class="d-flex align-items-center justify-content-center mx-auto">
        <div style="font-weight: bold; font-size: 24px;color: rgba(0, 0, 0, 50%);">您目前所在場館為 </div>
        <div style="font-weight: 800; font-size: 26px; color: rgba(0, 0, 0, 90%); margin-left: 10px;">
          {{
              $store.state.currentvenue
          }}
        </div>
      </div>
      <div v-if="$store.state.currvenue" class="d-flex" @emptyRegion="resEmpty">
        <ViewRegion v-for="item in maps" :key="item.id" :region="item"></ViewRegion>
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
      // regionamount: [],
      maps: [],
    };
  },
  methods: {
    async fetchApi() {
      let regions = []
      await axios({
        method: 'get',
        baseURL: this.$store.state.api,
        url: '/deviceInfo',
        'Content-Type': 'application/json',
      })
        .then((response) => regions = response.data)
        .catch((err) => { console.error(err) })


      regions.sort()
      console.log(regions)
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
    async fetchTableMap() {
      let tempmaps = []
      await axios({
        method: 'get',
        baseURL: this.$store.state.api + '/table/Map',
        'Content-Type': 'application/json',
      })
        .then((response) => tempmaps = response.data)
        .catch((err) => { console.error(err) })

      //尋訪/table/Map中之指定場館中所有區域 ( 包括已經無裝置的區域 )
      for (const key in tempmaps) {
        // console.log(key, maps[key]);
        if (tempmaps[key].Venue == this.$store.state.currentvenue) {
          this.maps.push(tempmaps[key])
        }
      }
    },
    resEmpty() {
      this.fetchTableMap()
      console.log('resEmpty')
    }
  },
  mounted() {
    this.fetchTableMap()
  },
};
</script>