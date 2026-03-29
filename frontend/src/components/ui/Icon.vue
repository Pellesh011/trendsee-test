<template>
  <span class="icon icon-16" :class="sizeClass">
    <img :src="src" :alt="alt" class="icon-img" />
  </span>
</template>

<script setup lang="ts">
import { computed } from 'vue'

interface Props {
  src: string
  size?: '16' | '20' | '32'
  alt?: string
  class?: string
}

const props = withDefaults(defineProps<Props>(), {
  size: '16',
  alt: 'Icon'
})

const sizeClass = computed(() => `icon-${props.size}`)
</script>

<style scoped>
.icon-img {
  object-fit: contain;
  width: 100%;
  height: 100%;
}
</style>

