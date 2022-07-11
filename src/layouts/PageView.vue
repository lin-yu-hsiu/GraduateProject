<template>
  <n-scrollbar x-scrollable style="max-height: 100vh;">
    <div style="background-color: #D9D9D9">
      <router-view />
    </div>
  </n-scrollbar>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  components: {
  }
});
</script>