<template>
  <div class="d-flex">
    <MenuBar></MenuBar>
    <div class="p-5 w-100 mx-auto d-flex justify-content-center align-items-center" style="height: 100vh">
      <h1 style="font-weight: bold; color: rgba(0, 0, 0, 30%); ">Welcome !</h1>
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
  },
});
</script>
