<template>
  <n-message-provider>
    <n-scrollbar x-scrollable style="max-height: 100vh;">
      <div style="background-color: #D9D9D9">
        <router-view v-if="isRouterActive" />
      </div>
    </n-scrollbar>
  </n-message-provider>

</template>
<script setup>

import { ref, provide, nextTick } from 'vue'
const isRouterActive = ref(true)
provide('reload', () => {
  isRouterActive.value = false
  nextTick(() => {
    isRouterActive.value = true
  })
})

</script>