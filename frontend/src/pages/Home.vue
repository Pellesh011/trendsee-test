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
    <button 
      v-if="postsStore.hasMore && !postsStore.loading"
      class="find-more-btn"
      @click="postsStore.loadMore"
    >
      Load More Posts
    </button>
    <p v-else-if="!postsStore.hasMore" class="no-more">No more posts</p>
    <div v-if="postsStore.loading" class="loading">Loading...</div>
    <div v-if="postsStore.error" class="error">{{ postsStore.error }}</div>
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
  postsStore.refreshPosts();
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
  padding: 12px 24px;
  background: linear-gradient(45deg, #ff6b6b, #feca57);
  color: white;
  border: none;
  border-radius: 25px;
  font-size: 16px;
  cursor: pointer;
  transition: transform 0.2s;
}

.find-more-btn:hover {
  transform: scale(1.05);
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

