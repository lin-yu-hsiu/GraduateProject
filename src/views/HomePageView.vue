<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
  </div>
</template>

<script>
// @ is an alias to /src
import { defineComponent } from "vue";
import MenuBar from "@/components/MenuBar.vue";

export default defineComponent({
  components: {
    MenuBar
  }
});
</script>
