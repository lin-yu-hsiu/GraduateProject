<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="d-flex p-5 w-100">
      <ViewRegion class="m-3"></ViewRegion>
      <ViewRegion class="m-3"></ViewRegion>
      <ViewRegion class="m-3"></ViewRegion>
    </div>
  </div>
</template>

<script>
import MenuBar from '@/components/MenuBar.vue';
import ViewRegion from '@/components/ViewRegion.vue';
export default {
  components: {
    MenuBar,
    ViewRegion
  },
  data() {
    return {

    };
  },
};
</script>