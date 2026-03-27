import { ref } from 'vue';
import axios from 'axios';
import type { Post, BackendPost, MyPostsResponse } from '@/types/post';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
});

export function useApi() {
  const loading = ref(false);
  const error = ref<string | null>(null);

  const fetchMyPosts = async (skip: number = 0, limit: number = 10): Promise<MyPostsResponse | null> => {
    try {
      loading.value = true;
      error.value = null;
      const token = localStorage.getItem('access_token') || '';
      const response = await api.get<MyPostsResponse>('/posts/me', {
        params: { skip, limit },
        headers: { 
          Authorization: `Bearer ${token}`
        }
      });
      return response.data;
    } catch (err) {
      error.value = 'Failed to fetch my posts';
      console.error(err);
      return null;
    } finally {
      loading.value = false;
    }
  };

  return { loading, error, fetchMyPosts };
}

