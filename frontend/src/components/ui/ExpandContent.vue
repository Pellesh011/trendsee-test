<template>
  <div class="expand-container">
    <div
      class="expand-content"
      :style="contentStyle"
      ref="contentWrapper"
      :aria-expanded="isOpen.toString()"
    >
      <slot>
        <!-- fallback content -->
        <p class="caption gray-8 text-lh-caption regular" v-html="modelValue"></p>
      </slot>
    </div>

    <button class="expand-button action-small semibold black" @click="toggle">
      {{ isOpen ? 'Свернуть' : 'Ещё' }}
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, nextTick, watch, onMounted } from 'vue'

interface Props {
  modelValue?: string
  maxCollapsedHeight?: number
  transitionMs?: number
}

const props = defineProps<Props & { modelValue: string }>()
const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

const isOpen = ref(false)
const contentWrapper = ref<HTMLElement | null>(null)
const contentFullHeight = ref<number>(0)

// defaults
const maxCollapsedHeight = props.maxCollapsedHeight ?? 80
const transitionMs = props.transitionMs ?? 300

const contentStyle = computed(() => {
  const height = isOpen.value ? `${contentFullHeight.value}px` : `${maxCollapsedHeight}px`
  return {
    height,
    overflow: 'hidden',
    transition: `height ${transitionMs}ms ease`,
  } as Record<string, string>
})

async function updateFullHeight(): Promise<void> {
  await nextTick()
  const el = contentWrapper.value
  if (!el) return
  // temporarily let it auto-size to measure
  const prevHeight = el.style.height
  el.style.height = 'auto'
  // scrollHeight gives full content height
  contentFullHeight.value = el.scrollHeight
  el.style.height = prevHeight
}

async function toggle(): Promise<void> {
  await updateFullHeight()
  isOpen.value = !isOpen.value
  // if opening, set explicit height to trigger transition to full height
  if (isOpen.value && contentWrapper.value) {
    // Force a reflow to ensure transition applies
    void contentWrapper.value.offsetHeight
    // contentStyle computed will provide the target height
  }
}

watch(
  () => props.modelValue,
  async () => {
    await updateFullHeight()
    emit('update:modelValue', props.modelValue)
  }
)

onMounted(() => {
  updateFullHeight()
})
</script>

<style scoped>
.expand-container {
  width: 100%;
}

.expand-content {
  /* height/overflow/transition managed via inline style */
}

.expand-button {
  margin-top: 8px;
  background: none;
  border: none;
  padding: 0px;
  cursor: pointer;

  font-weight: 600;
}

.caption {
  margin: 0;
}
</style>
