import { ref } from 'vue';
import axios from 'axios';
import type { Post, BackendPost, MyPostsResponse } from '@/types/post';
import { router } from '@/router';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
});

// Global interceptor for 401 Unauthorized - redirect to login
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('access_token');
      router.push('/login');
    }
    return Promise.reject(error);
  }
);

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

  
  const login = async (name: string): Promise<{ access_token: string } | null> => {
    try {
      loading.value = true;
      error.value = null;
      const response = await api.post('/users/login', { name });
      const { access_token } = response.data;
      localStorage.setItem('access_token', access_token);
      return response.data;
    } catch (err: any) {
      error.value = err.response?.data?.detail || 'Login failed';
      console.error(err);
      return null;
    } finally {
      loading.value = false;
    }
  };

  return { loading, error, fetchMyPosts, login };
}



