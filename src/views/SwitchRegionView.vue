<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex p-5 w-100">
      <SwitchRegion class="m-3" v-for="item in regions" :key="item.id" :region="item"></SwitchRegion>
    </div>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue';
import SwitchRegion from '@/components/SwitchRegion.vue';


const regions = [
  {
    name: 'A 棟',
    thumbnail: 'regionpic1'
  },
  {
    name: 'B 棟',
    thumbnail: 'regionpic2'
  },
  {
    name: 'C 棟',
    thumbnail: 'regionpic2'
  },
]

export default {
  components: {
    MenuBar,
    SwitchRegion
  },
  data() {
    return {
      regions: regions
    };
  },
};
</script>