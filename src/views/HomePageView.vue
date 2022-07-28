<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="p-5 h-100 w-100 mx-auto">

    </div>
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
