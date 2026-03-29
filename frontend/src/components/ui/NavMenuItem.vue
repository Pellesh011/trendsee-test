<template>
  <li class="sub-menu-item">
    <a :href="href" class="horizontal-align">
      <Icon :src="props.iconSrc" />
      <span class="text-secondary menu-text body-medium">{{ label }}</span>
      <span v-if="badge" :class="badge.class">{{ badge.text }}</span>
    </a>
  </li>
</template>
<script setup lang="ts">

import Icon from './Icon.vue'

interface Badge { text: string; class: string }
interface Props { iconSrc: string; label: string; href: string; badge?: Badge }

const props = defineProps<Props>()

</script>
<style scoped>
.sub-menu-item .menu-text {
  margin-left: 10px;
}

.sub-menu-item .badger {
  margin-left: 20px;
  border-radius: 16px;
  padding: 4px 8px;
}
</style>
