<template>
  <div class="spinner-overlay">
    <img 
      src="@/assets/images/utils/131.gif" 
      alt="Loading spinner" 
      class="spinner-gif"
    />
  </div>
</template>

<script setup lang="ts">
// Full-screen GIF spinner component
</script>

<style scoped>
.spinner-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  backdrop-filter: blur(2px);
}

.spinner-gif {
  width: 80px;
  height: 80px;
  object-fit: contain;
}
</style>

