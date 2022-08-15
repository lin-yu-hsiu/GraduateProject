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
      <div class="w-100 d-flex justify-content-end">
        <div class="editRegion">
          <div class="editMode">
            編輯模式
            <n-switch v-model:value="this.$store.state.deviceEditMode" style="margin-left: 10px;" />
          </div>
          <router-link :to="{ name: 'addregion' }">
            <button v-if="this.$store.state.deviceEditMode" class="AddRegion my-1">
              新增區域
            </button>
          </router-link>
          <!-- <button v-if="this.$store.state.deviceEditMode" class="RemoveRegion mb-1">
            刪除區域
          </button> -->
        </div>
      </div>


      <div v-if="$store.state.currvenue && mapFlag" class="d-flex flex-wrap" @ifEmpty="ifEmpty_ViewDevice">
        <ViewRegion v-for="item in maps" :key="item.id" :region="item" @_reDisplay="reDisplay"></ViewRegion>
      </div>

      <div v-if="mapFlag == false"
        style="font-weight: 800; font-size: 22px; color: rgba(0, 0, 0, 70%); margin-top: 25vh; text-align: center;">
        目前
        {{
            $store.state.currentvenue
        }}館
        無任何區域，請移至新增區域此功能
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { inject } from "vue";
import MenuBar from '@/components/MenuBar.vue';
import ViewRegion from '@/components/ViewRegion.vue';


export default {
  setup() {
    const reload = inject('reload')
    const update = () => {
      reload()
    }
    return {
      update
    }
  },
  components: {
    MenuBar,
    ViewRegion
  },
  data() {
    return {
      maps: [],
      mapFlag: false,
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
          this.mapFlag = true
        }
      }
      // console.log(this.maps)
    },
    ifEmpty_ViewDevice() {
      this.fetchTableMap()
      this.update()
    },
    reDisplay() {
      this.maps = []
      this.fetchTableMap()
    }
  },
  mounted() {
    this.fetchTableMap()
    if (this.$store.state.currvenue == false) {
      this.$router.push('/')
    }

  },
};
</script>

<style scoped>
.editRegion {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: center;
  padding: 4px 8px;
  /* box-shadow: 0 0 5px 5px rgba(0, 0, 0, 0.1);
  background-color: transparent;
  border-radius: 5px; */
}

.editMode {
  display: flex;
  justify-content: end;
  align-items: center;
  font-weight: bold;
  font-size: 18px;
  border-radius: 5px;
  box-shadow: 0 0 5px 5px rgba(0, 0, 0, 0.1);
  width: 140px;
  padding: 5px 5px;
  transition: all 0.2s ease;
}

.AddRegion {
  font-weight: bold;
  font-size: 18px;
  border-radius: 5px;
  box-shadow: 0 0 5px 5px rgba(0, 0, 0, 0.1);
  width: 130px;
  padding: 5px 5px;
  border: none;
  outline: none;
  transition: all 0.2s ease;
}

.AddRegion:hover {
  background-color: rgba(215, 215, 215, 0.8);
  color: rgb(0, 200, 83);
  width: 155px;
}

.RemoveRegion {
  font-weight: bold;
  font-size: 18px;
  border-radius: 5px;
  box-shadow: 0 0 5px 5px rgba(0, 0, 0, 0.1);
  width: 130px;
  padding: 5px 5px;
  border: none;
  outline: none;
  transition: all 0.2s ease;
}

.RemoveRegion:hover {
  background-color: rgba(215, 215, 215, 0.8);
  color: rgba(215, 2, 2, 1);
  width: 155px;
}
</style>