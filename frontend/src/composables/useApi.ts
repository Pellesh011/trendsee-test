import { ref } from 'vue';
import axios from 'axios';
import type { Post } from '@/types/post';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
});

export function useApi() {
  const loading = ref(false);
  const error = ref<string | null>(null);

  const fetchPosts = async (): Promise<Post[] | null> => {
    try {
      loading.value = true;
      error.value = null;
      // Mock API response for now (backend /posts not implemented)
      await new Promise(resolve => setTimeout(resolve, 1000));
      return [
        {
          id: 6,
          image: 'https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=1000',
          stats: ['150k', '120k', '25k', '780'],
          desc: 'Load more reels demo',
          username: '@demo',
          followers: '500K',
          likes: '150K'
        }
      ];
    } catch (err) {
      error.value = 'Failed to fetch posts';
      console.error(err);
      return null;
    } finally {
      loading.value = false;
    }
  };

  return { loading, error, fetchPosts };
}

