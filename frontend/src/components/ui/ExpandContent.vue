<template>
  <div class="expand-container" :class=" background">
    <div class="expand-content" :style="contentStyle" ref="contentWrapper" >
      <slot>
        <!-- fallback content -->
        <p class="" v-html="modelValue"></p>
      </slot>
    </div>

    <div class=" expand-btn">

      <button class="expand-button action-small semibold black flex " :class="expandBtnAlign" @click="toggle">
        <div v-if="expandIcon" class="mr-5">
          <div class=" icon-16">
            <div v-if="isOpen">
              <img :src="`src/assets/images/icons/arrow-down.svg`" alt="views" class="rotate-180">
            </div>
            <div v-if="!isOpen">
              <img :src="`src/assets/images/icons/arrow-down.svg`" alt="views">
            </div>

          </div>
        </div>
        <span class="">
        {{ isOpen ? 'Свернуть' : 'Ещё' }}
        </span>
      </button>

    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, computed, nextTick, watch, onMounted } from 'vue'

interface Props {
  modelValue?: string
  maxCollapsedHeight?: number
  transitionMs?: number
  classes?: string
  expandBtnAlign?: string
  expandBtn?: boolean
  expandIcon?: boolean
  background?: string
}

const props = defineProps<Props & { modelValue: string; expandIcon: boolean; expandBtnAlign: string, classes: string , background: string}>()
const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

const isOpen = ref(false)
const contentWrapper = ref<HTMLElement | null>(null)
const contentFullHeight = ref<number>(0)

// defaults
const maxCollapsedHeight = props.maxCollapsedHeight ?? 80
// const transitionMs = props.transitionMs ?? 300

const contentStyle = computed(() => {
  const height = isOpen.value ? `${contentFullHeight.value}px` : `${maxCollapsedHeight}px`
  return {
    height,
    overflow: 'hidden',
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
.rotate-180{
  transform: rotateX(180deg);
}

.expand-btn {
 height: 20px;
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

.right {
  position: absolute;
  right: 30px;
}
</style>
