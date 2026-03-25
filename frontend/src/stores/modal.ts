import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { Post } from '@/types/post';

export const useModalStore = defineStore('modal', () => {
  const activePost = ref<Post | null>(null);

  const openPost = (post: Post) => {
    activePost.value = { ...post };
  };

  const close = () => {
    activePost.value = null;
  };

  return { activePost, openPost, close };
});

