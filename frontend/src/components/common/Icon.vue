<template>
  <span class="icon icon-16" :class="sizeClass">
    <img :src="icon" :alt="alt" class="icon-img" />
  </span>
</template>

<script setup lang="ts">
import { computed } from 'vue'


const icons = import.meta.glob('/src/assets/images/icons/*.svg', {
  eager: true,
  import: 'default'
}) as Record<string, string>

const iconMap = Object.fromEntries(
  Object.entries(icons).map(([path, value]) => {
    const name = path.split('/').pop()?.replace('.svg', '')
    return [name, value]
  })
)

const icon = computed((): string => {
  return iconMap[props.src] ?? ''
})

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

