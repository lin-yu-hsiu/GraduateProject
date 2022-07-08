<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex p-5 w-100">
      <SwitchRegion class="m-3"></SwitchRegion>
      <SwitchRegion class="m-3"></SwitchRegion>
      <SwitchRegion class="m-3"></SwitchRegion>
    </div>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue';
import SwitchRegion from '@/components/SwitchRegion.vue';
export default {
  components: {
    MenuBar,
    SwitchRegion
  },
  data() {
    return {

    };
  },
};
</script>