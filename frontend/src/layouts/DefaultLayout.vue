<template>
  <div class="layout-container container">
    <router-view />
  </div>
</template>

<script setup lang="ts">
// Layout composes sidebar + content

</script>

<style scoped>
.layout-container {
  display: flex !important;
  height: 100vh;
  width: 100vw;
  max-width: 100%;
  overflow: hidden;
  margin: 0;
  padding: 0;
}
.container {
  max-width: none !important;
  width: 100%;
  height: 100%;
}
</style>


