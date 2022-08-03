<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex flex-column p-5 mx-auto w-100">
      <div style="font-weight: bold; font-size: 18px;color: rgba(0, 0, 0, 30%); align-self: flex-start;">
        /
        {{
            $store.state.currentvenue
        }}
        / 查看裝置
      </div>
      <div class="d-flex align-items-center justify-content-center mx-auto">
        <div style="font-weight: bold; font-size: 24px;color: rgba(0, 0, 0, 50%);">您目前所在場館為 </div>
        <div style="font-weight: 800; font-size: 26px; color: rgba(0, 0, 0, 90%); margin-left: 10px;">
          {{
              $store.state.currentvenue
          }}
        </div>
      </div>
      <div v-if="$store.state.currvenue" class="d-flex" @ifEmpty="ifEmpty_ViewDevice">
        <ViewRegion v-for="item in maps" :key="item.id" :region="item" @_reDisplay="reDisplay"></ViewRegion>
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
      maps: [],
    };
  },
  methods: {
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
      console.log(this.maps)
    },
    ifEmpty_ViewDevice() {
      // console.log('viewdevice')
      this.fetchTableMap()
    },
    reDisplay() {
      console.log('redisplay region')
      this.maps = []
      this.fetchTableMap()
    }
  },
  mounted() {
    this.fetchTableMap()
  },
};
</script>