<template>
<div class="content" ref="contentRef">
    <div class="reels-grid">
      <ReelItem
        v-for="post in postsStore.posts"
        :key="post.id"
        :post="post"
        @open-reel="modalStore.openPost($event)"
      />
    </div>

    <div v-if="postsStore.loading" class="loading">Loading...</div>
    <div v-if="postsStore.error" class="error">{{ postsStore.error }}</div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue';
import { usePostsStore } from '@/stores/posts';
import { useModalStore } from '@/stores/modal';
import ReelItem from '@/components/ui/ReelItem.vue';
import type { Post } from '@/types/post';

const postsStore = usePostsStore();
const modalStore = useModalStore();

let rafId: number;
const checkScroll = () => {
  const content = contentRef.value;
  console.log(postsStore.hasMore)
  if (!content || postsStore.loading || !postsStore.hasMore) return;
  
  const { scrollTop, scrollHeight, clientHeight } = content;
  console.log('scrollTop:', scrollTop, 'clientHeight:', clientHeight, 'scrollHeight:', scrollHeight, 'distance from bottom:', scrollHeight - (scrollTop + clientHeight));
  if (scrollTop + clientHeight >= scrollHeight - 500) {
    postsStore.loadMore();
  }
};

const throttledScroll = () => {

  rafId = requestAnimationFrame(checkScroll);
};

const contentRef = ref<HTMLDivElement>();

onMounted(() => {
  postsStore.refreshPosts();
  contentRef.value?.addEventListener('scroll', throttledScroll);
});

onUnmounted(() => {
  contentRef.value?.removeEventListener('scroll', throttledScroll);
  if (rafId) cancelAnimationFrame(rafId);
});
</script>

<style scoped>
.content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

.reels-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 20px;
  margin-bottom: 20px;
}

.no-more, .loading, .error {
  text-align: center;
  padding: 20px;
  color: #666;
}

.loading {
  color: #feca57;
}

.error {
  color: #ff6b6b;
}
</style>

