<template>
  <div class="video-statistics">
    <div class="video-statistics-container">
      <div class="flex">
        <div v-for="stat in stats" :key="stat.label" class="column">
          <div class="image-container">
            <Icon :src="stat.icon" size="20" />
          </div>
          <div class="stats caption text-lh-caption regular">{{ stat.value }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Icon from './Icon.vue'

interface Stat {
  icon: string
  value: string
  label?: string
}

interface Props {
  stats: Stat[]
}

const props = defineProps<Props>() // eslint-disable-next-line @typescript-eslint/no-unused-vars
</script>

<style scoped>
.video-statistics {
  display: flex;
  justify-content: space-between;
  max-width: 254px;
  margin: 0 auto;
  position: absolute;
  bottom: 0px;
  width: 100%;
}

.video-statistics-container {
  margin: 10px;
  border: 1px solid transparent;
  border-radius: 8px;
  width: 100%;
  backdrop-filter: blur(8px);
  background-color: var(--Black-40, #00000066);
}

.video-statistics .stats {
  color: white;
  padding-bottom: 5px;
}

.column {
  flex: 1;
  padding: 0px;
  text-align: center;
}

.image-container {
  width: 100%;
  padding: 5px;
}

.image-container :deep(.icon-img) {
  width: 20px;
  height: 20px;
}
</style>

