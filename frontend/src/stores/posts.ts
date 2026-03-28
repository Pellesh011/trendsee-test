import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { Post, BackendPost, MyPostsResponse } from '@/types/post';
import { useApi } from '@/composables/useApi';

function backendPostToPost(bp: BackendPost): Post {
  const date = new Date(bp.created_at).toLocaleDateString();
  const idNum = parseInt(bp.id.slice(-6)) || Math.floor(Math.random() * 1000);
  const views = Math.floor(Math.random() * 100 + 10).toLocaleString() + 'k';
  const likesNum = Math.floor(Math.random() * 80 + 5);
  const likesStr = likesNum + 'k';
  const commentsNum = Math.floor(Math.random() * 15 + 1);
  const commentsStr = commentsNum + 'k';
  const shares = Math.floor(Math.random() * 500 + 100);

  return {
    id: idNum,
    image: '/src/assets/images/utils/video-preview.png',
    videoUrl: 'https://sample-videos.com/zip/10/mp4/SampleVideo_1280x720_1mb.mp4',
    stats: [views, likesStr, commentsStr, shares.toString()],
    desc: `${bp.title.slice(0,50)}... ${bp.text.slice(0,100)}`,
    username: '@myaccount',
    followers: 'Your account',
    likes: likesStr,
    date
  };
}

export const usePostsStore = defineStore('posts', () => {
  const posts = ref<Post[]>([]);
  const hasMore = ref(true);
  const total = ref(0);
  let currentSkip = 0;
  const limit = 10;
  const { loading, error, fetchMyPosts } = useApi();

  const loadMyPosts = async () => {
    const response = await fetchMyPosts(currentSkip, limit);
    if (response) {
      const newPosts = response.items.map(backendPostToPost);
      posts.value.push(...newPosts);
      currentSkip += limit;
      total.value = response.total;
      hasMore.value = response.items.length === limit;
    } else {
      hasMore.value = false;
    }
  };

  const loadMore = async () => {
    await loadMyPosts();
  };

  const refreshPosts = async () => {
    posts.value = [];
    currentSkip = 0;
    hasMore.value = true;
    await loadMyPosts();
  };

  return { 
    posts, 
    loading, 
    error, 
    loadMore, 
    loadMyPosts, 
    refreshPosts,
    hasMore 
  };
});

