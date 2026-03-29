<template>
  <button :class="buttonClass" v-bind="$attrs">
    <Icon :src="iconSrc" :size="iconSize" />
    <span v-if="text" class="text">{{ text }}</span>
  </button>
</template>

<script setup lang="ts">
import Icon from '../common/Icon.vue'

interface Props {
  iconSrc: string
  text?: string
  size?: 'sm' | 'lg'
}

const props = withDefaults(defineProps<Props>(), {
  size: 'sm'
})

import { computed } from 'vue'

const buttonClass = computed(() => `icon-button-${props.size}`)
const iconSize = computed(() => props.size === 'lg' ? '20' : '16')
</script>

<style scoped>
.icon-button-sm {
  display: flex;
  align-items: center;
  padding: 6px;
  gap: 6px;
  background-color: var(--Black-40, #00000066);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 12px;
  margin-bottom: 4px;
}

.icon-button-lg {
  display: flex;
  align-items: center;
  padding: 8px;
  gap: 8px;
  background-color: var(--Black-40, #00000066);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 12px;
  margin-bottom: 4px;
}

.icon-button span.text {
  margin-left: 4px;
}
</style>

