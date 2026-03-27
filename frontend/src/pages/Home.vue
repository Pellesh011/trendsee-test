<template>
  <div class="content">
    <div class="reels-grid">
      <ReelItem
        v-for="post in postsStore.posts"
        :key="post.id"
        :post="post"
        @open-reel="modalStore.openPost($event)"
      />
    </div>
  
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { usePostsStore } from '@/stores/posts';
import { useModalStore } from '@/stores/modal';
import ReelItem from '@/components/ui/ReelItem.vue';
import type { Post } from '@/types/post';

const postsStore = usePostsStore();
const modalStore = useModalStore();

onMounted(() => {
  // Initial load if needed
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

.find-more-btn {
  display: block;
  margin: 20px auto;
}
</style>

