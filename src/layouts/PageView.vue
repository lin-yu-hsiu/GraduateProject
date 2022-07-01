<template>
  <n-scrollbar class="d-flex" style="max-height: 100vh;">
    <MenuBar></MenuBar>
    <ContentBlock></ContentBlock>
  </n-scrollbar>
</template>

<script>
import { defineComponent } from "vue";

import MenuBar from './MenuBar.vue'
import ContentBlock from './ContentBlock.vue'

export default defineComponent({
  components: {
    MenuBar,
    ContentBlock
  }
});
</script>