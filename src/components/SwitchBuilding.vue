<template>
  <div class="regionList" @click="switchVenue">
    <div style=" font-weight: bold; font-size: 26px;">{{ regionInfo.name }}</div>
    <button class="detailBtn p-0" v-if="this.$store.state.venueEditMode" @click="removeVenue"
      @mouseover="icon = remove_hover" @mouseleave="icon = remove">
      <img :src="icon" style="width: 36px; height: 42px; z-index: 10;">
    </button>
  </div>
</template>

<script>
import axios from 'axios'
import { defineComponent, inject } from "vue";
import remove from '../assets/pic/trash.png'
import remove_hover from '../assets/pic/trash_hover.png'

export default defineComponent({
  setup() {
    const reload = inject('reload')
    const update = () => {
      reload()
    }
    return {
      update,
    }
  },
  props: {
    region: {
      required: true
    }
  },
  data() {
    return {
      icon: remove,
      remove: remove,
      remove_hover: remove_hover,


      //
      regionInfo: this.region,
      removeflag: false,
    }
  },
  methods: {
    switchVenue() {
      if (this.$store.state.venueEditMode == false) {
        this.$store.commit('switchRegion', this.regionInfo.name);
      }
    },
    async removeVenue() {

      const body = {
        'Venue': this.regionInfo.name,
      }
      const json = JSON.stringify(body);

      await axios({
        method: 'post',
        baseURL: this.$store.state.api + '/deleteVenue',
        headers: { 'Content-Type': 'application/json' },
        data: json
      })
        .then((response) => response = response.data)
        .catch((error) => console.log(error))

      this.removeflag = true
      this.$emit('removeDisplay', this.regionInfo.name, this.removeflag) //刪除此場館並回傳到父元件以更新畫面
    },
    te() {

    }
  },
  mounted() {

  },
});
</script>

<style scoped>
.regionList {
  width: 300px;
  height: 180px;
  background: linear-gradient(to bottom, #ffffff 0%, rgba(142, 142, 142, 50%) 100%);
  box-shadow: 0 10px 10px 0 rgba(0, 0, 0, 25%);
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-radius: 20px;
  padding: 20px;
}

.regionList:hover {
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 5%) inset;
}

.thumbNail {
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 25%);
  width: 300px;
  height: 150px;
  border-radius: 20px;
}

.detailBtn {
  background-color: transparent;
  border: none;
  z-index: 10;
}
</style>