<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import MenuBar from "@/components/MenuBar.vue";

export default defineComponent({
  components: {
    MenuBar
  }
});
</script>
